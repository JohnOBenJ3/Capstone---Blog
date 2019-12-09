from django.urls import path
from . import views

# These are the same as the urlpatterns in the django_blog urls file.
# But, you don't need the admin url in this file because it is already
# in the main urls file.
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('posts/', views.post, name='blog-post'),
    # Cannot have underscores in url patterns.
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail')
]