from django.db import models
from accounts.models import User
from recipe.models import Recipe

# Create your models here

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)