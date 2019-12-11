import os
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, BadHeaderError
from .models import Posts
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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
    # print("Success!")
    return render(request, 'blog/contact.html')

# This function should take the form and if it is a proper post request
# send the email to my email I used in the settings file.
def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            try:
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                message = request.POST.get('message')
                
                recipient = ['orrin24johnson@gmail.com']
                
                send_mail(name,
                          email,
                          phone,
                          message,
                          recipient,
                          fail_silently=False)
                
            except BadHeaderError:
                return HttpResponse('Bad Header Found')
            
    return redirect('blog/index.html')
                