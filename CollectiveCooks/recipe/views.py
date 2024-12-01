from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddRecipeForm
from .models import Recipe
from accounts.models import User

@login_required
def add_recipe_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = AddRecipeForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.username = request.user
            recipe.save()

            messages.add_message(request, messages.SUCCESS, "Recipe Submitted", extra_tags='success')
            return render(request, 'add_recipe.html', {'form': form})
        else:
            messages.add_message(request, messages.ERROR, "Recipe Not Submitted. Please correct your inputs", extra_tags='recipe_message_error')
            print(form.errors)
    else:
        form = AddRecipeForm(user=request.user)

    return render(request, 'add_recipe.html', {'form': form})

def recipe_detail(request, username, recipe_id):
    user = get_object_or_404(User, username=username)
    recipe = get_object_or_404(Recipe, id=recipe_id, username=user)
    return render(request, 'view_recipe.html', {'recipe': recipe, 'user': user})