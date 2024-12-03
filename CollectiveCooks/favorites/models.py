from django.db import models
from accounts.models import User
from recipe.models import Recipe

# Create your models here

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id','recipe_id')

    def __str__(self):
        return f"{self.user_id} favorited {self.recipe_id}"
    
class UserReport(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    report_detail = models.TextField(max_length=254, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reports")

    class Meta:
        unique_together = ('reporter', 'user_id')

    def __str__(self):
        return f"Report for User {self.user_id.username} by {self.reporter.username} ID: {self.user_id.id}"


class RecipeReport(models.Model):
    recipe_id = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    report_detail = models.TextField(max_length=254, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_reports")
    
    class Meta:
        unique_together = ('reporter', 'recipe_id')

    def __str__(self):
        return f"Report for Recipe {self.recipe_id.title} by {self.reporter.username}"