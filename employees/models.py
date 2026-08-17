from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='skills_through')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=1, help_text="1–10")

    class Meta:
        unique_together = ('employee', 'skill')

    def __str__(self):
        return f"{self.employee} - {self.skill} (level {self.level})"


class EmployeeImage(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='employee_images/')
    order = models.PositiveIntegerField(help_text="Порядковый номер для сортировки")

    class Meta:
        ordering = ['order']  # сортировка по порядку

    def __str__(self):
        return f"Image {self.order} for {self.employee}"


@receiver(post_delete, sender=EmployeeImage)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
