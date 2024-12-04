from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddRecipeForm
from .models import Recipe, Comment
from accounts.models import User
from favorites.models import Favorite, RecipeReport

@login_required(login_url="/auth/login")
def add_recipe_view(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            # Save the new recipe
            recipe = form.save(commit=False)
            recipe.username = request.user
            recipe.save()

            # Add success message and redirect
            messages.success(request, "Recipe Submitted", extra_tags='recipe_message')
            return render(request, 'add_recipe.html', {'form': form})
        else:
            # Add error message if form is invalid
            messages.error(request, "Recipe Not Submitted. Please correct your inputs", extra_tags='recipe_message_error')

    else:
        form = AddRecipeForm(user=request.user)

    return render(request, 'add_recipe.html', {'form': form})

@login_required(login_url="/auth/login")
def recipe_detail(request, username, recipe_id):
    user = get_object_or_404(User, username=username)
    recipe = get_object_or_404(Recipe, id=recipe_id, username=user)
    has_reported = RecipeReport.objects.filter(recipe_id=recipe.id, reporter=request.user).exists()
    is_favorite = Favorite.objects.filter(user_id=user.id,recipe_id=recipe.id)

    if request.method == 'POST':
        # Handling comment submission
        if 'comment' in request.POST:
            comment_text = request.POST.get('comment').strip()
            
            if comment_text:
                # Create and save the comment
                comment = Comment(recipe=recipe, user=request.user, text=comment_text)
                comment.save()
                
                messages.success(request, "Comment added successfully!", extra_tags='comment_success')
            else:
                messages.error(request, "Comment cannot be empty", extra_tags='comment_error')

        # Handling rating submission
        elif 'rating' in request.POST:
            rating = int(request.POST.get('rating', 0))
            
            if rating > 0:
                recipe.total_rating += rating
                recipe.total_reviews += 1
                recipe.save()
                
                messages.success(request, "Thank you for rating!", extra_tags='rating_success')
            else:
                messages.error(request, "Invalid rating submission", extra_tags='rating_error')

        # Redirect back to the same recipe page to avoid form resubmission on refresh
        return redirect('recipe:recipe_detail', username=username, recipe_id=recipe_id)

    return render(request, 'view_recipe.html', {'recipe': recipe, 'user': user, 'has_reported': has_reported, 'is_favorite': is_favorite})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.username:
        recipe.delete()
        return redirect('auth:profile', request.user.id)
    return redirect('recipe:view_recipe.html', recipe_id)

@login_required(login_url="/auth/login")
def add_to_favorites(request, username, recipe_id):
    user = get_object_or_404(User, username=username)
    recipe = get_object_or_404(Recipe, id=recipe_id)


    favorite, created = Favorite.objects.get_or_create(user_id=user, recipe_id=recipe)

    if not created:
        favorite.delete()

    is_favorite = created

    has_reported = RecipeReport.objects.filter(recipe_id=recipe.id, reporter=request.user).exists()


    return render(request, 'view_recipe.html', {
        'user': recipe.username ,
        'recipe': recipe,
        'is_favorite': is_favorite,
        'has_reported' : has_reported
    })

@login_required(login_url="/auth/login")
def report_recipe(request,username,recipe_id):
    reported_recipe = get_object_or_404(Recipe, id=recipe_id)
    user = get_object_or_404(User, username=username)


    if request.method == "POST":
        report_detail = request.POST.get("report_detail", "").strip()
        
        if report_detail:
            RecipeReport.objects.create(reporter=request.user, recipe_id=reported_recipe, report_detail=report_detail)
            messages.success(request, "Recipe reported successfully.")
        else:
            messages.error(request, "Please provide details for the report.")

    return redirect('recipe:recipe_detail', username=user.username, recipe_id=reported_recipe.id)

# View to edit a comment
def edit_comment(request, comment_id, username):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Check if the logged-in user is the one who created the comment
    if request.user != comment.user:
        return redirect('recipe:recipe_detail', username=comment.recipe.username.username, recipe_id=comment.recipe.id)

    if request.method == "POST":
        # Get the updated text from the POST request
        new_text = request.POST.get('text')
        
        if new_text:
            # Update the comment text and save it
            comment.text = new_text
            comment.save()

            # Redirect to the recipe detail page after editing the comment
            return redirect('recipe:recipe_detail', username=comment.recipe.username.username, recipe_id=comment.recipe.id)

    # Render the edit comment form
    return render(request, 'edit_comment.html', {'comment': comment})


# View to delete a comment
def delete_comment(request, comment_id, username):
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the logged-in user is the one who created the comment
    if request.user != comment.user:
        return redirect('recipe:recipe_detail', username=comment.recipe.username.username, recipe_id=comment.recipe.id)

    if request.method == 'POST':
        # Delete the comment if the user is the comment creator
        comment.delete()
        # Redirect to the recipe detail page after deleting the comment
        return redirect('recipe:recipe_detail', username=comment.recipe.username.username, recipe_id=comment.recipe.id)

    # If the method is not POST, render a confirmation page (optional, if you want to confirm before deletion)
    return render(request, 'confirm_delete_comment.html', {'comment': comment})

