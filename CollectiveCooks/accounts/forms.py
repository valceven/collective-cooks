from django import forms  
from .models import User 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LogInForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control'
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
        fields = ['first_name','last_name','username','email','gender','birthdate','password1','password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('This email already exists in the database!')
        return email
    
class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    gender = forms.ChoiceField(
        choices=User.Gender.choices,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    birthdate = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'birthdate', 'avatar']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already associated with another account.')
        return email