from django.db import models

STATUSES = [
    ("COMPLETED", "Completed"),
    ("PENDING", "Pending"),
    ("CANCELED", "Canceled"),
]


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    status = models.CharField(
        max_length=128, choices=STATUSES, default="PENDING")

    def __str__(self):
        return self.name
