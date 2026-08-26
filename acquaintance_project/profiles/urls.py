from django.urls import path
from .views import ProfileListView, RandomProfileView

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list'),
    path('random/', RandomProfileView.as_view(), name='random-profile'),
]
