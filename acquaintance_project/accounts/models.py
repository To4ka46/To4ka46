from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    bio = models.TextField(blank=True, verbose_name="О себе")
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, verbose_name="Фото профиля")

    def __str__(self):
        return self.username or self.email

