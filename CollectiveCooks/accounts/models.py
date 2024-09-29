from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):

    first_name = None
    last_name = None

    class Gender(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F',('Female')
        OTHER = 'O',('Other')

    birthdate = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)
    details = models.TextField(max_length=254, null=True, blank=True)   

    def __str__(self):
        return f"{self.username} {self.email}"  