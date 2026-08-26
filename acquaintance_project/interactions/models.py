from django.conf import settings
from django.db import models

ACTION_CHOICES = [('like', 'Лайк'), ('dislike', 'Дизлайк')]

class Interaction(models.Model):
    """Лайк/дизлайк от user к target_profile"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='interactions_given')
    target_profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='interactions_received')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'target_profile')  # один раз на профиль


class ViewedProfile(models.Model):
    """История просмотренных профилей"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='viewed_profiles')
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)


class Match(models.Model):
    """Взаимные лайки (совпадение)"""
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_1')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_2')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')
