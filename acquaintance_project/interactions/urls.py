from django.urls import path
from .views import (
    LikeDislikeView,
    ViewedProfilesListView,
    LikedProfilesListView,
    DislikedProfilesListView,
)

urlpatterns = [
    # Лайк/дизлайк с передачей action через kwargs
    path('<int:target_id>/like/', LikeDislikeView.as_view(), {'action': 'like'}, name='like'),
    path('<int:target_id>/dislike/', LikeDislikeView.as_view(), {'action': 'dislike'}, name='dislike'),

    # Списки взаимодействий
    path('viewed/', ViewedProfilesListView.as_view(), name='viewed-profiles'),
    path('liked/', LikedProfilesListView.as_view(), name='liked-profiles'),
    path('disliked/', DislikedProfilesListView.as_view(), name='disliked-profiles'),
]
