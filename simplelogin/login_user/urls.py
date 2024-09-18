from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('register/', views.contact_view, name='users'),
    path('register/success/', views.register_success, name='register_success'),
]
