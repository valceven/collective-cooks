from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('add/', views.add_recipe_view, name="add_recipe"),
    path('<str:username>/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('favorites/<str:username>/<int:recipe_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('report/<str:username>/<int:recipe_id>/', views.report_recipe, name="report_recipe"),
    path('<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<str:username>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('recipe/<str:username>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
