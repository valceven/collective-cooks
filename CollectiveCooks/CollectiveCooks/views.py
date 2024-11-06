from django.shortcuts import render
from django.db.models import Count
from accounts.models import User

def homepage(request):
    
    popular_users = User.objects.annotate(follower_count=Count('followers')).order_by('-follower_count')[:5]
    return render(request, 'home.html', { 'popular_users' : popular_users }) 

def about(request):
  return render(request, 'about.html')
