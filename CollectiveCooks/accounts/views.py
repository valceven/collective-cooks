from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LogInForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data('email')
            password = form.cleaned_data('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Congratulations You are now logged in.")
                return redirect('')
            else:
                messages.error(request, "invalid email or password. pleae try again")
        else:
            messages.error(request,'Please fix your inputs')
    else:
        form = LogInForm()

    return render(request, 'login/login_page.html', {'form': form})



def register_view(request):
    return HttpResponse("This is the register page!")