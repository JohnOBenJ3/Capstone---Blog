from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# need to make a model for the Blog Post 
class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
