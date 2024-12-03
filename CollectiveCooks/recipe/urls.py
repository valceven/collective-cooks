from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('add/', views.add_recipe_view, name="add_recipe"),
    path('<str:username>/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('favorites/<str:username>/<int:recipe_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('report/<str:username>/<int:recipe_id>/', views.report_recipe, name="report_recipe"),
]
