from django.db import models

class Workspace(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название рабочего места')
    location = models.CharField(max_length=200, verbose_name='Расположение')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name