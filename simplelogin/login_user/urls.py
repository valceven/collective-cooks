from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('register/', views.contact_view, name='register'),
    path('register/success/', views.register_success, name='register_success'),
    path('login/', views.login_view, name="login"),
    path('login/success/',views.login_success, name="login_success"),
]
