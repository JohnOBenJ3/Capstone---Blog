from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')


def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post.html', context)


def contact(request):
    return render(request, 'blog/contact.html')

    
