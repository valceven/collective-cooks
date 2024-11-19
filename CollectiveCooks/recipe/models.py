from django.db import models
from accounts.models import User
from django.utils import timezone

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Snack', 'Snack'),
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, default="Food")
    rating = models.FloatField(default=0.0)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, null=False, default="No Input")
    procedures = models.CharField(max_length=1000, null=False, default="No Input")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Breakfast')
    ingredients = models.CharField(max_length=255, default="No Input")
    ingredients_count = models.CharField(max_length=255, default="1")
    image = models.ImageField(default="default_food.png", null=True)

    def __str__(self):
        return self.title

