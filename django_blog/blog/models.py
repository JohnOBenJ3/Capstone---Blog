from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# need to make a model for the Blog Post 
class Post(model.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
