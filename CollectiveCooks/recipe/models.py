from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=254)



class Ingredient(models.Model):
    name = models.CharField(max_length=254)