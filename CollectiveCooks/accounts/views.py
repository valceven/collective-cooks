from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import LogInForm, RegistrationForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from favorites.models import Favorite
from recipe.models import Recipe
from .models import User, Follow
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q


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
            login(request,user)
            return redirect('homepage')
        else :
            return render(request, 'register/register_page.html', {'form': form})
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

    followers = Follow.objects.filter(following=user)
    following = Follow.objects.filter(follower=user)
    self_following = Follow.objects.filter(follower=request.user, following=user)
    
    for follow in followers:
        follow.is_self_following = Follow.objects.filter(follower=request.user, following = follow.follower).exists()


    context = {
        'user': user,
        'favorites': favorites,
        'recipes': recipes,
        'following': following,
        'followers': followers,
        'self_following': self_following,
        'followers_count': followers.count(),
        'following_count': following.count(),
    }

    return render(request, 'profile/profile.html', context)


@login_required(login_url="/auth/login")
def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.user != user:
        messages.error(request, "You are not allowed to edit this profile.")
        return redirect('auth:profile', user_id=request.user.id)

    form = EditProfileForm(instance=user)
    password_form = PasswordChangeForm(user)

    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            form = EditProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('auth:profile', user_id=user_id)
            else:
                messages.error(request, 'Please correct the errors in your profile.')
                password_form = PasswordChangeForm(user)  # Reset password form
        
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
                messages.success(request, 'Your password has been updated!')
                return redirect('auth:profile', user_id=user_id)
            else:
                messages.error(request, 'Please correct the errors in your password.')
                form = EditProfileForm(instance=user) 

    return render(request, 'profile/edit_profile.html', {
        'form': form,
        'password_form': password_form
    })

@login_required(login_url="auth/login")
def follow_user(request, user_id ):
    if request.method == "POST":
        user_to_follow = get_object_or_404(User, id=user_id)

        if user_to_follow != request.user:
            follow, created = Follow.objects.get_or_create(follower = request.user, following=user_to_follow)

            if not created:
                follow.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def search_user(request):
    query = request.GET.get('q', '')
    users = []

    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | 
            Q(email__icontains=query)
        )

    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'search/search_results.html', context)

def about(request):
    return render(request, 'about.html')