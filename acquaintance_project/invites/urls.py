from django.urls import path
from .views import InviteCreateView, InviteListView, InviteActionView

urlpatterns = [
    # Создать приглашение: POST /api/invites/<receiver_id>/invite/
    path('<int:receiver_id>/invite/', InviteCreateView.as_view(), name='create-invite'),

    # Список всех приглашений пользователя: GET /api/invites/invites/
    path('invites/', InviteListView.as_view(), name='invites-list'),

    # Принять/отклонить приглашение: PATCH/PUT /api/invites/<pk>/action/
    path('<int:pk>/action/', InviteActionView.as_view(), name='invite-action'),
]
