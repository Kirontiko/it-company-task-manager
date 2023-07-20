from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255,
                            unique=True)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position,
                                 related_name="workers",
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("UI", "Urgent Important"),
        ("UNI", "Urgent Not Important"),
        ("NUI", "Not Urgent Important"),
        ("NUNI", "Not Urgent Not Important")
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=4)
    task_type = models.ForeignKey(TaskType,
                                  related_name="tasks",
                                  on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker,
                                       related_name="tasks")

