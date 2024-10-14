from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login', views.login_view, name="login"),
    path('register',views.register_view, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
