from django.urls import path
from . import views

# These are the same as the urlpatterns in the django_blog urls file.
# But, you don't need the admin url in this file because it is already
# in the main urls file.
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/', views.post, name='blog-post'),
    # Cannot have underscores in url patterns.
    path('latest-posts/', views.latest_posts, name='latest-posts'),
    path('announcements/', views.announcements, name='announcements')
]