from django.db import models
from accounts.models import User
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=50, null=False, default="Food")
    rating = models.FloatField(default=0.0)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, null=False, default="No Input")
    procedure = models.CharField(max_length=255, null=False, default="No Input")
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __str__(self):
        return self.title
