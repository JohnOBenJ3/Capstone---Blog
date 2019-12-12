from django.urls import path
from . import views

# These are the same as the urlpatterns in the django_blog urls file.
# But, you don't need the admin url in this file because it is already
# in the main urls file.
urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('posts/', views.post, name='blog-post'),
    # Cannot have underscores in url patterns.
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
    path('<slug:slug>/delete/', views.delete_post, name='delete-post'),
    path('<slug:slug>/edit/', views.edit_post, name='edit-post'),
]