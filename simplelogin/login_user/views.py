from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse


# Create your views here.
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            contact = form.cleaned_data['contact']
            return render(request, 'users/success.html', {'name' : name})
        
    else: 
        form = ContactForm()

    return render(request, 'users/register.html', {'form': form})

def register_success(request):
    return HttpResponse("Registration Successful!")