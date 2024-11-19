from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('add/', views.add_recipe_view, name="add_recipe"),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
