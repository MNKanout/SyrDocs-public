from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

class BlogPost(models.Model):
    """A blog post"""
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """Retrun a string representation of blog"""
        return self.text
