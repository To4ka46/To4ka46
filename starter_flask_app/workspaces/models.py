from django.db import models
from django.db import models
from employees.models import EmployeeProfile

class Workplace(models.Model):
    desk_number = models.CharField("Номер стола", max_length=20, unique=True)
    extra_info = models.TextField("Дополнительная информация", blank=True)

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"

    def __str__(self):
        return f"Стол {self.desk_number}"

    employee = models.OneToOneField(
        'employees.EmployeeProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='workplace',
        verbose_name="Сотрудник"
    )

class Workplace(models.Model):
    desk_number = models.CharField("Номер стола", max_length=20, unique=True)
    extra_info = models.TextField("Дополнительная информация", blank=True)
    employee = models.OneToOneField(
        EmployeeProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='workplace',
        verbose_name="Сотрудник"
    )

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"

    def __str__(self):
        base = f"Стол {self.desk_number}"
        if self.employee:
            return f"{base} ({self.employee})"
        return base