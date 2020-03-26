from django import forms
from .models import BlogPost

class BlogPostform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category','title','text']
        labels = {'title':'Blog post title', 'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
