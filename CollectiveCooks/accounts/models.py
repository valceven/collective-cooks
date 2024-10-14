from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):

    first_name = None
    last_name = None

    class Gender(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F', ('Female')
        OTHER = 'O', ('Other')

    birthdate = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)
    details = models.TextField(max_length=254, null=True, blank=True)   

    # New fields for profile
    bio = models.TextField(blank=True, null=True)  # User's short bio or description
    following = models.IntegerField(default=0)     # Number of people the user is following
    followers = models.IntegerField(default=0)     # Number of followers the user has
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')  # Profile picture

    def __str__(self):
        return self.username
