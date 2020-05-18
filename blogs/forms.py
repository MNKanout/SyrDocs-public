from django import forms
from .models import BlogPost
from tinymce.widgets import TinyMCE

class BlogPostform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category','title','text']
        labels = {'title':'Blog post title', 'text':''}
        widgets = {'text':TinyMCE(attrs={'cols': 80, 'rows': 30})}
