from django.db import models
from accounts.models import User


# Create your models here

class Favorite(models.Model):
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )