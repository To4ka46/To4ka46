from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class EmployeeProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    description = models.TextField("Описание", blank=True)  # сюда потом подключите WYSIWYG

    class Meta:
        verbose_name = "Профиль сотрудника"
        verbose_name_plural = "Профили сотрудников"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    name = models.CharField("Навык", max_length=50, unique=True)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class EmployeeSkill(models.Model):
    LEVEL_CHOICES = [(i, str(i)) for i in range(1, 11)]

    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField("Уровень (1–10)", choices=LEVEL_CHOICES)

    class Meta:
        unique_together = ('employee', 'skill')  # чтобы не было дублей навыков у одного сотрудника
        verbose_name = "Навык сотрудника"
        verbose_name_plural = "Навыки сотрудников"

    def __str__(self):
        return f"{self.employee} — {self.skill} (уровень {self.level})"