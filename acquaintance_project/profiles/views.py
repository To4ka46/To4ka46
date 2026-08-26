# profiles/views.py
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['gender', 'city', 'status']
    ordering_fields = ['age', 'likes_count']

class RandomProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        qs = Profile.objects.all()
        # можно добавить фильтры по запросу: ?gender=M&city=Moscow
        gender = self.request.query_params.get('gender')
        city = self.request.query_params.get('city')
        status = self.request.query_params.get('status', 'searching')

        if gender: qs = qs.filter(gender=gender)
        if city: qs = qs.filter(city=city)
        qs = qs.filter(status=status)

        # исключить себя
        user_id = self.request.user.id
        qs = qs.exclude(user_id=user_id)

        # исключить уже просмотренные (опционально)
        viewed_ids = set(
            self.request.user.viewed_profiles.values_list('profile_id', flat=True)
        )
        qs = qs.exclude(id__in=viewed_ids)

        return qs.order_by('?').first()  # случайный
