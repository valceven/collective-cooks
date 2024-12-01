from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddRecipeForm
from .models import Recipe, Comment
from accounts.models import User

@login_required
def add_recipe_view(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.username = request.user
            recipe.save()

            messages.add_message(request, messages.SUCCESS, "Recipe Submitted", extra_tags='success')
            return render(request, 'add_recipe.html', {'form': form})
        else:
            messages.add_message(request, messages.ERROR, "Recipe Not Submitted. Please correct your inputs", extra_tags='recipe_message_error')
    else:
        form = AddRecipeForm(user=request.user)

    return render(request, 'add_recipe.html', {'form': form})

@login_required
def recipe_detail(request, username, recipe_id):
    user = get_object_or_404(User, username=username)
    recipe = get_object_or_404(Recipe, id=recipe_id, username=user)

    if request.method == 'POST':
        # Handling comment submission
        if 'comment' in request.POST:
            comment_text = request.POST.get('comment').strip()
            
            if comment_text:
                # Create and save the comment
                comment = Comment(recipe=recipe, user=request.user, text=comment_text)
                comment.save()
                
                messages.add_message(request, messages.SUCCESS, "Comment added successfully!", extra_tags='comment_success')
            else:
                messages.add_message(request, messages.ERROR, "Comment cannot be empty", extra_tags='comment_error')

        # Handling rating submission
        elif 'rating' in request.POST:
            rating = int(request.POST.get('rating', 0))
            
            if rating > 0:
                recipe.total_rating += rating
                recipe.total_reviews += 1
                recipe.save()
                
                messages.add_message(request, messages.SUCCESS, "Thank you for rating!", extra_tags='rating_success')
            else:
                messages.add_message(request, messages.ERROR, "Invalid rating submission", extra_tags='rating_error')

        # Redirect back to the same recipe page to avoid form resubmission on refresh
        return redirect('recipe:recipe_detail', username=username, recipe_id=recipe_id)

    return render(request, 'view_recipe.html', {'recipe': recipe, 'user': user})
