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
        # Get ingredients and procedures as a list from the POST data
        # ingredients_list = self.data.getlist('ingredient')
        # ingredients_count_list = self.data.getlist('amount')
        # procedures_list = self.data.getlist('procedure')

        # print(f"ingredient: {ingredients_list}")
        # print(f"count: {ingredients_count_list}")
        # print(f"procedure: {procedures_list}")
        
        # Combine ingredients into a string for saving
        # cleaned_data['ingredients'] = ', '.join(ingredients_list)
        # cleaned_data['ingredients_count'] = ', '.join(ingredients_count_list)
        # cleaned_data['procedures'] = '\n'.join(procedures_list)
        
        # print(f"ingredient: {cleaned_data['ingredients']}")
        # print(f"ingredient: {cleaned_data['ingredients_count']}")
        # print(f"ingredient: {cleaned_data['procedures']}")

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
