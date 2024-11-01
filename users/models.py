from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.TextChoices):
    DRIVER = 'DR', 'Driver'
    PASSENGER = 'PA', 'Passenger'

class TaskUser(AbstractUser):
    user_type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.PASSENGER,
    )
    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"


class Day(models.Model):
    name = models.CharField(max_length=9)  # e.g., "Sunday", "Monday"

    def __str__(self):
        return self.name


class User():
    days_practicing = models.ManyToManyField(Day)
