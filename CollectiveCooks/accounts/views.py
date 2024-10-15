from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import LogInForm, RegistrationForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from favorites.models import Favorite
from recipe.models import Recipe
from .models import User

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = LogInForm(data=request.POST or None)  # Simplified handling

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.POST.get('next', 'homepage'))
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        messages.error(request, 'Please fix your inputs. Errors: {}'.format(form.errors))

    return render(request, 'login/login_page.html', {'login_form': form})


def register_view(request):

    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('homepage')
        else :
            messages.error(request, 'Please fix your inputs.')
    else:
        form = RegistrationForm()

    return render(request, 'register/register_page.html', {'form': form})

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('homepage')


@login_required(login_url="/auth/login")
def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id) 

    favorites = Favorite.objects.filter(user_id=user)
    recipes = Recipe.objects.filter(username=user)

    context = {
        'user': user,
        'favorites': favorites,
        'recipes': recipes,
    }

    return render(request, 'profile/profile.html', context)

@login_required(login_url="/auth/login")
def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.user != user:
        messages.error(request, "You are not allowed to edit this profile.")
        return redirect('auth:profile', user_id=request.user.id)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('auth:profile', user_id=user_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'profile/edit_profile.html', {'form': form})
