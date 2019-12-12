import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse, BadHeaderError
from .models import Posts
from .forms import ContactForm, UpdateForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.contrib import admin

# Create your views here.

class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'blog/post_detail.html'
    
class PostList(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    
    



# def home(request):
#     return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')


def post(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/post.html', context)


# def contact(request):
    # print("Success!")
    # return render(request, 'blog/contact.html')

# This function should take the form and if it is a proper post request
# send the email to my email I used in the settings file.
def contact(request):
    return render(request, 'blog/contact.html')


def delete_post(request, slug):
    obj = get_object_or_404(Posts, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
        
    context = {
        "object": obj
    }
    
    return render(request, 'blog/post_delete.html', context)


def edit_post(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    form = UpdateForm(instance=post)
    print('EDITING')
    if request.method == "POST":
        form = UpdateForm(request.POST)
        print('METHOD IS POST')
        print(request)
        post.title = request.POST.get('title')
        post.slug = request.POST.get('slug')
        post.content = request.POST.get('content')
        post.status = request.POST.get('status')
        if form.is_valid():
            print('Form is:', form)
            form.save(commit=True)
            
        post.save()
        return redirect('/')
    context = {
        'form': form
    }

    return render(request, 'blog/edit_post.html', context)
    
        
    
    
                