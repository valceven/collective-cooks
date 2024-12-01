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
    total_reviews = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=False, default="No Input")
    procedures = models.TextField(null=False, default="No Input")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Breakfast')
    ingredients = models.TextField(default="No Input")
    ingredients_count = models.TextField(default="1")
    image = models.ImageField(default="default_food.png", null=True)

    def __str__(self):
        return self.title
    
    def get_amounts_and_ingredients(self):
        ingredients_list = self.ingredients.split('\n')
        amounts_list = self.ingredients_count.split('\n')
        return zip(amounts_list, ingredients_list)
    
    def get_procedures(self):
        return self.procedures.split('\n')