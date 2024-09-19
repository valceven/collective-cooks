from django.shortcuts import render, redirect
from .forms import ContactForm, AuthenticationFormWithInactiveUsersOkay
from django.http import HttpResponse
from django.contrib.auth import login
from .models import User

# Create your views here.
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("NICE KA DOL")
            user = form.save(commit=False)
            user.save()
            return redirect('users:register')
    else:
        form = ContactForm()

    return render(request, 'users/register.html', {'form': form})

def register_success(request):
    return HttpResponse("Registration Successful!")

def login_view(request):
    form = AuthenticationFormWithInactiveUsersOkay()
    
    if request.method == "POST":
        print("IM POSTED")
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            try:
                user = User.objects.get(username=username)
                print(user)
                if user.check_password(password):
                    login(request, user)
                    return redirect('users:login_success')
                else:
                    print("Invalid password")
            except User.DoesNotExist:
                print("User does not exist")
        else:
            print("Username and password must be provided")

    return render(request, 'users/login.html', {'form': form})

def login_success(request):
    return HttpResponse("Login Successful! Welcome, {}!".format(request.user.username))
