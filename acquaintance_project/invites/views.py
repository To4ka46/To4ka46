from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Invite
from .serializers import InviteSerializer


class InviteCreateView(generics.CreateAPIView):
    serializer_class = InviteSerializer

    def perform_create(self, serializer):
        sender = self.request.user
        receiver_id = self.kwargs.get('receiver_id')

        if not receiver_id:
            return Response({'error': 'receiver_id обязателен'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            receiver_id = int(receiver_id)
        except (ValueError, TypeError):
            return Response({'error': 'receiver_id должен быть числом'}, status=status.HTTP_400_BAD_REQUEST)

        if sender.id == receiver_id:
            return Response({'error': 'Нельзя отправить приглашение себе'}, status=status.HTTP_400_BAD_REQUEST)

        # Ищем существующее приглашение между этими пользователями
        invite, created = Invite.objects.get_or_create(
            sender=sender,
            receiver_id=receiver_id,
            defaults={'message': serializer.validated_data.get('message', ''), 'status': 'pending'}
        )

        if not created:
            # Если приглашение уже есть, не меняем статус автоматически.
            # Разрешаем обновить только сообщение, если оно передано
            if 'message' in serializer.validated_data:
                invite.message = serializer.validated_data['message']
                # Важно: не сбрасываем статус на pending, чтобы не ломать логику «уже отклонено»
                invite.save()

        return Response(InviteSerializer(invite).data, status=status.HTTP_201_CREATED)


class InviteListView(generics.ListAPIView):
    serializer_class = InviteSerializer

    def get_queryset(self):
        user = self.request.user
        # Показываем все приглашения, где пользователь — отправитель или получатель
        return Invite.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).select_related('sender', 'receiver').order_by('-created_at')


class InviteActionView(generics.UpdateAPIView):
    serializer_class = InviteSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # Пользователь может принимать/отклонять только те приглашения, где он получатель
        return Invite.objects.filter(receiver=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        status_action = request.data.get('status')

        allowed_statuses = ['accepted', 'rejected']
        if status_action not in allowed_statuses:
            return Response(
                {'error': f'Допустимые статусы: {", ".join(allowed_statuses)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        instance.status = status_action
        instance.save()

        return Response(InviteSerializer(instance).data)
