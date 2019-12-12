from django import forms
from .models import Posts


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'slug', 'content', 'status']