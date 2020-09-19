from django.db import models

# Create your models here.
from django.utils import timezone

class Game(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    best_cricketer = models.CharField(max_length=32, null=True, blank=True)
    white = models.CharField(max_length=32, null=True, blank=True)
    yellow = models.CharField(max_length=32, null=True, blank=True)
    orange = models.CharField(max_length=32, null=True, blank=True)
    green = models.CharField(max_length=32, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
