from django.shortcuts import render, redirect
from .forms import AddRecipeForm

# Create your views here.
def add_recipe_view(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AddRecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
