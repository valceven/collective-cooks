from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login', views.login_view, name="login"),
    path('register',views.register_view, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('profile/<int:user_id>/', views.profile_view, name="profile"),
    path('profile/<int:user_id>/edit', views.edit_profile, name="edit_profile"),
    path('profile/<int:user_id>/follow/', views.follow_user, name="follow_user"),
    path('about/', views.about, name='about'),
    path('search/',views.search_user, name='search_user'),
]