from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)  
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'username']
        labels = {
            'name': 'Your name',
            'email': 'Your email',
            'contact': 'Uniques Style Username',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    pass
