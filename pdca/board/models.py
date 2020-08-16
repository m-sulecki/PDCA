from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    problem = models.TextField()
    action = models.TextField()
    date_notification = models.DateTimeField(default=timezone.now)
    in_charge = models.ForeignKey(User, on_delete=models.CASCADE)


