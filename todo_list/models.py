from django.conf import settings
from django.db import models
from django.utils import timezone

CHOICES = (('low', 'low'),
           ('medium', 'medium'),
           ('high', 'high'))

class Goal(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField(max_length=500, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=False)
    is_completed = models.BooleanField(blank=True, default=False)
    priority = models.CharField(max_length=10, choices=CHOICES, default = 'high')

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
