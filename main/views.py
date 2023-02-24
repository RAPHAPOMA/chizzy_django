from django.shortcuts import render
from .models import AiplugPost

# Create your views here.

def home_page(request):
    posts = AiplugPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context)
