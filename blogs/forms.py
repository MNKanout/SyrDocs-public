from django import forms
from .models import BlogPost
from ckeditor.widgets import CKEditorWidget

class BlogPostform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category','title','text']
        labels = {'title':'Blog post title', 'text':''}
        widgets = {'text':CKEditorWidget(attrs={'cols': 80, 'rows': 30})}
