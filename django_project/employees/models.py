from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta

ROLE_CHOICES = [
    ('backend', 'Backend разработчик'),
    ('frontend', 'Frontend разработчик'),
    ('fullstack', 'Fullstack разработчик'),
    ('tester', 'Тестировщик'),
    ('manager', 'Менеджер'),
    ('designer', 'Дизайнер'),
]

GENDER_CHOICES = [
    ('M', 'Мужской'),
    ('F', 'Женский'),
    ('O', 'Другой'),
]

SKILL_LEVEL_CHOICES = [
    ('beginner', 'Начинающий'),
    ('intermediate', 'Средний'),
    ('advanced', 'Продвинутый'),
    ('expert', 'Эксперт'),
]

class Skill(models.Model):
    name = models.CharField('Название навыка', max_length=100, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES)
    role = models.CharField('Роль', max_length=20, choices=ROLE_CHOICES)
    desk_number = models.IntegerField('Номер стола')
    hire_date = models.DateField('Дата приёма на работу')
    skills = models.ManyToManyField(Skill, through='EmployeeSkill', related_name='employees')

    class Meta:
        ordering = ['-hire_date']

    @property
    def tenure_days(self):
        from django.utils import timezone
        today = timezone.now().date()
        return (today - self.hire_date).days

    def clean(self):
        """Валидация соседства столов для тестировщиков и разработчиков"""
        if self.role in ['backend', 'frontend', 'fullstack']:
            # Ищем тестировщиков рядом
            nearby_desks = [self.desk_number - 1, self.desk_number + 1]
            neighbors = Employee.objects.filter(desk_number__in=nearby_desks, role='tester')
            if neighbors.exists():
                raise ValidationError(
                    f'Нельзя сажать разработчика рядом с тестировщиком. '
                    f'На столах {", ".join(str(d) for d in nearby_desks)} уже работают тестировщики.'
                )
        elif self.role == 'tester':
            # Ищем разработчиков рядом
            nearby_desks = [self.desk_number - 1, self.desk_number + 1]
            neighbors = Employee.objects.filter(
                desk_number__in=nearby_desks,
                role__in=['backend', 'frontend', 'fullstack']
            )
            if neighbors.exists():
                raise ValidationError(
                    f'Нельзя сажать тестировщика рядом с разработчиком. '
                    f'На столах {", ".join(str(d) for d in nearby_desks)} уже работают разработчики.'
                )

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'


class EmployeeImage(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Фото', upload_to='employee_images/')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Фото {self.employee} #{self.order}'


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField('Уровень', max_length=20, choices=SKILL_LEVEL_CHOICES)

    class Meta:
        unique_together = ('employee', 'skill')
