from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):

    HIGH = 3
    MEDIUM = 2
    SMALL = 1

    LEVELS = (
        (HIGH, "high"),
        (MEDIUM, "medium"),
        (SMALL, "small"),
    )

    problem = models.TextField()
    action = models.TextField()
    date_notification = models.DateTimeField(default=timezone.now)
    planed_date = models.DateTimeField(default=timezone.now)
    done_date = models.DateTimeField(default=timezone.now)
    in_charge = models.ForeignKey(User, on_delete=models.CASCADE)
    importance = models.IntegerField(choices=LEVELS, default=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})