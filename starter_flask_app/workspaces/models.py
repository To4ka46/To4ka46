from django.db import models

class Workplace(models.Model):
    desk_number = models.CharField(max_length=20, verbose_name='Номер рабочего места')
    extra_info = models.TextField(blank=True, verbose_name='Дополнительная информация')

    employee = models.OneToOneField(
        'employees.EmployeeProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='workplace',
        verbose_name='Сотрудник'
    )

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"

    def __str__(self):
        base = f"Стол {self.desk_number}"
        if self.employee:
            return f"{base} ({self.employee})"
        return base
