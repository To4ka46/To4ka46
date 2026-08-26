from rest_framework import generics, status
from rest_framework.response import Response
from .models import Interaction, Match, ViewedProfile
from .serializers import InteractionSerializer, ViewedProfileSerializer
from profiles.models import Profile


class LikeDislikeView(generics.CreateAPIView):
    serializer_class = InteractionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        target_id = self.kwargs.get('target_id')
        action = self.kwargs.get('action')  # 'like' или 'dislike'

        if not target_id or not action:
            return Response({'error': 'target_id и action обязательны'}, status=status.HTTP_400_BAD_REQUEST)

        # Нельзя взаимодействовать со своим профилем
        if int(target_id) == user.id:
            return Response({'error': 'Нельзя взаимодействовать со своим профилем'}, status=status.HTTP_400_BAD_REQUEST)

        # Обновляем или создаём взаимодействие
        interaction, created = Interaction.objects.update_or_create(
            user=user,
            target_profile_id=target_id,
            defaults={'action': action}
        )

        # Логика совпадения (Match) только при лайке
        if action == 'like':
            reverse_like = Interaction.objects.filter(
                user_id=target_id,
                target_profile__user=user,
                action='like'
            ).exists()
            if reverse_like:
                Match.objects.get_or_create(
                    user1=min(user.id, int(target_id)),
                    user2=max(user.id, int(target_id))
                )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewedProfilesListView(generics.ListAPIView):
    serializer_class = ViewedProfileSerializer

    def get_queryset(self):
        return self.request.user.viewed_profiles.select_related('profile').order_by('-viewed_at')


class LikedProfilesListView(generics.ListAPIView):
    serializer_class = Profile  # важно: здесь нужен сериализатор, а не модель

    # Исправление: импортируем ProfileSerializer из profiles.serializers
    from profiles.serializers import ProfileSerializer
    serializer_class = ProfileSerializer

    def get_queryset(self):
        liked_ids = Interaction.objects.filter(
            user=self.request.user,
            action='like'
        ).values_list('target_profile_id', flat=True)
        return Profile.objects.filter(id__in=liked_ids)


class DislikedProfilesListView(generics.ListAPIView):
    from profiles.serializers import ProfileSerializer
    serializer_class = ProfileSerializer

    def get_queryset(self):
        disliked_ids = Interaction.objects.filter(
            user=self.request.user,
            action='dislike'
        ).values_list('target_profile_id', flat=True)
        return Profile.objects.filter(id__in=disliked_ids)
