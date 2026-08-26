from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GENDER_CHOICES = [('M', 'Мужской'), ('F', 'Женский'), ('O', 'Другой')]
STATUS_CHOICES = [
    ('searching', 'В поиске'),
    ('taken', 'Занят'),
    ('not_interested', 'Не заинтересован'),
]
PRIVACY_CHOICES = [
    ('public', 'Публичный'),
    ('friends', 'Только для лайкнувших'),
    ('private', 'Приватный'),
]

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(120)]
    )
    city = models.CharField(max_length=100, blank=True)
    interests = models.TextField(blank=True, help_text="через запятую или JSON")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='searching')
    privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES, default='public')
    likes_count = models.PositiveIntegerField(default=0)  # денормализация для скорости
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} profile"


class Photo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='profile_photos/')
    is_main = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        # если ставим главную, убираем у других
        if self.is_main:
            self.profile.photos.update(is_main=False)
        super().save(*args, **kwargs)
