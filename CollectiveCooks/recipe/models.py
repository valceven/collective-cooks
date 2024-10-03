from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    procedure = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Ingredient(models.Model):
    name = models.CharField(max_length=254)