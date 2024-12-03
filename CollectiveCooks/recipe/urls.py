from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('add/', views.add_recipe_view, name="add_recipe"),
    path('<str:username>/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('<int:id>/edit/', views.edit_recipe, name='edit_recipe'),
]
