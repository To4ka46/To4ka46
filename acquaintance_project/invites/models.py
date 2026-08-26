from django.conf import settings
from django.db import models

STATUS_INVITE = [
    ('pending', 'Ожидает'),
    ('accepted', 'Принято'),
    ('rejected', 'Отклонено'),
]

class Invite(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invites_sent')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invites_received')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_INVITE, default='pending')
    contact_info = models.TextField(blank=True, help_text="телефон, TG, etc. после принятия")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sender', 'receiver')
