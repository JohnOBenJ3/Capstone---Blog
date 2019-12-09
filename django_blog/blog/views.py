from django.shortcuts import render
from django.views import generic
# from django.http import HttpResponse
from .models import Posts
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'blog/post_detail.html'
    
class PostList(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    
    
context = {
    'posts': Posts.objects.all()
}


# def home(request):
#     return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')


def post(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/post.html', context)


def contact(request):
    return render(request, 'blog/contact.html')




    
