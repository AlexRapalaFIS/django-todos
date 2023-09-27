from django.db import models
from django.contrib.auth.models import User

STATUSES = [
    ("COMPLETED", "Completed"),
    ("PENDING", "Pending"),
    ("CANCELED", "Canceled"),
]


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=128)
    status = models.CharField(
        max_length=128, choices=STATUSES, default="PENDING")

    def __str__(self):
        return self.name
