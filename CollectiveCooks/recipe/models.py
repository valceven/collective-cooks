from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    title = models.CharField(max_length=50, null=False, default="Food")
    rating = models.FloatField(default=0.0)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, null=False, default="No Input")
    procedure = models.CharField(max_length=255, null=False, default="No Input")

    def __str__(self):
        return self.title  # It's better to return the title for easier identification.

class Ingredient(models.Model):
    name = models.CharField(max_length=254)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=1)  # Set a default recipe ID here

    def __str__(self):
        return self.name  # Return the ingredient name for better identification.
