from django import forms  
from .models import Recipe
from django.utils import timezone

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'category', 'ingredients', 'ingredients_count', 'procedures', 'image']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddRecipeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

    def save(self, commit=True):
        instance = super(AddRecipeForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        instance.rating = 0.0
        instance.created_date = timezone.now()
        if commit:
            instance.save()
        return instance
