from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True,label="Your name", max_length=100)
    email = forms.EmailField(required=True,label="Your email")
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    phone = forms.CharField(max_length=10)
