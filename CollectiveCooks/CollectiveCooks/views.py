from django.shortcuts import render
from django.db.models import Count
from accounts.models import User
from recipe.models import Recipe

def homepage(request):
    # Get the top 5 most popular users based on follower count
    popular_users = User.objects.annotate(follower_count=Count('followers')).order_by('-follower_count')[:5]

    # Get the top 10 recipes, sorted first by total_reviews, then by get_rating for recipes with the same reviews
    top_recipes = Recipe.objects.all().order_by('-total_reviews')[:10]

    # Now, we will sort the recipes by get_rating for those with the same total_reviews count
    top_recipes = sorted(top_recipes, key=lambda recipe: (-recipe.total_reviews, -recipe.get_rating()))

    return render(request, 'home.html', {
        'popular_users': popular_users,
        'top_recipes': top_recipes,  # Pass the top recipes to the template
    })


def about(request):
  return render(request, 'about.html')