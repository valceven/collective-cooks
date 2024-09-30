from django import forms  
from .models import User 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LogInForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control'  # You can also add other classes here
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control'
        })
    )
    class Meta: 
        model = User
        fields = ['username','password']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255,required=True)
    gender = forms.ChoiceField(choices=User.Gender.choices, required=True)
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username','email','gender','birthdate','password1','password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('This email already exists in the database!')
        return email