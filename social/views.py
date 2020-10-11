from django.shortcuts import render
from .models import *

def feed(request):
    posts = Post.objects.all()

    context = { 'posts': posts}
    return render(request, 'social/feed.html', context)

def profile(request):
    return render(request, 'social/profile.html')
