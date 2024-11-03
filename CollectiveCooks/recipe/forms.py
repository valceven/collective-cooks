from django import forms  
from .models import Recipe
from django.utils import timezone

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'procedure']

        title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter title'}))   
        description = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter description'}))
        procedure = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter procedure'}))

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('Username', 1)
            super(Recipe, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            instance = super(Recipe, self).save(commit=False)
            if self.user:
                instance.user = self.user
            instance.rating = 0.0 
            instance.created_date = timezone.now()  
            if commit:
                instance.save()
            return instance