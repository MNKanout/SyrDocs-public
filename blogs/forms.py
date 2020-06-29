from django import forms
from .models import BlogPost
from tinymce.widgets import TinyMCE

class BlogPostform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category','title','text']
        labels = {'title':'Post title', 'text':''}
        widgets = {'text':TinyMCE(attrs={'cols': 80, 'rows': 30,'spellchecker':True})}
