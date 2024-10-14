from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F',('Female')
        OTHER = 'O',('Other')

    birthdate = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)
    details = models.TextField(max_length=254, null=True, blank=True)
    avatar = models.ImageField(default="default_avatar.png", null=True)   

    def __str__(self):
        return self.username