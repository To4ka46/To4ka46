from django.db import models

from workspaces.models import Workspace

class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    position = models.CharField(max_length=100, verbose_name='Должность')
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Рабочее место'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'