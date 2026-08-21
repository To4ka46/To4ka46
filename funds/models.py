from django.conf import settings
from django.db import models
from django.utils import timezone

class Collect(models.Model):
    OCCASION_CHOICES = [
        ("birthday", "День рождения"),
        ("wedding", "Свадьба"),
        ("anniversary", "Годовщина"),
        ("moving", "Переезд"),
        ("other", "Другое"),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="collects")
    title = models.CharField(max_length=200)
    occasion = models.CharField(max_length=50, choices=OCCASION_CHOICES)
    description = models.TextField(blank=True)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)  # None = «бесконечный» сбор
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cover_image = models.ImageField(upload_to="collect_covers/", blank=True, null=True)
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.author})"

    @property
    def is_active(self):
        return timezone.now() < self.end_at


class Payment(models.Model):
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE, related_name="payments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ["-paid_at"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # обновляем current_amount сбора
        self.collect.current_amount = self.collect.payments.aggregate(
            total=models.Sum("amount")
        )["total"] or 0
        self.collect.save(update_fields=["current_amount"])
