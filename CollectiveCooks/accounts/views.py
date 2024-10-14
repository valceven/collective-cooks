from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LogInForm, RegistrationForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LogInForm(data=request.POST) 

        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("User authenticated")
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            print("Form errors:", form.errors) 
            messages.error(request, 'Please fix your inputs. Errors: {}'.format(form.errors))
    else:
        form = LogInForm()

    return render(request, 'login/login_page.html', {'login_form': form})


def register_view(request):
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

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('homepage')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile/profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('auth:profile')  # Correctly references the namespaced profile URL
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditProfileForm(instance=request.user)  # Pre-fill the form with the current user data

    context = {
        'form': form,
    }
    return render(request, 'profile/edit_profile.html', context)