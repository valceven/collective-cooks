from django import forms  
from .models import Recipe
from django.utils import timezone

class AddRecipeForm(forms.ModelForm):
    # makes the text fields be empty
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter title'
        })
    )   
    description = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter description'
        })
    )
    procedure = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter procedure'
        })
    )
    ingredients = forms.CharField(
        widget = forms.Textarea(attrs={
            'placeholder': 'Enter ingredients, one per line...',
            'rows': 4
        }),
        help_text="Please enter each ingredient on a new line.",
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'procedure', 'ingredients']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddRecipeForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddRecipeForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        instance.rating = 0.0 
        instance.created_date = timezone.now()  
        if commit:
            instance.save()
        return instance

    def clean_ingredients(self):
        ingredients = self.cleaned_data['ingredients'].splitlines()
        ingredients = [ingredient.strip() for ingredient in ingredients if ingredient.strip()]
        return ingredients
