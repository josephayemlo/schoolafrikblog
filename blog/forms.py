from django import forms
from .models import BlogPost
from django_ckeditor_5.widgets import CKEditor5Widget

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = BlogPost
        fields = ['title', 'content' ]