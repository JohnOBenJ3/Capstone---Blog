from django.shortcuts import render
from django.views import generic
# from django.http import HttpResponse
from .models import Posts

# Create your views here.

class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'blog/post_detail.html'
    
class PostList(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('create_on')
    template_name = 'index.html'
    
    
context = {
    'posts': Posts.objects.all()
}


def home(request):
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')


def post(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/post.html', context)


def contact(request):
    return render(request, 'blog/contact.html')

    
