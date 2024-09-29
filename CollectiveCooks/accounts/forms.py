from django import forms  
from .models import User 
from django.contrib.auth.forms import UserCreationForm

class LogInForm(forms.ModelForm):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['email','password']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255,required=True)
    gender = forms.ChoiceField(choices=User.Gender.choices, required=True)

    class Meta:
        model = User
        fields = ['email','gender','birthdate','details','password1','password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('This email already exists in the database!')
        return email