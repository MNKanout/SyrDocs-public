from django.db import models
from django.contrib.auth.models import User

from blogs.models import BlogPost

class Dictionary(models.Model):
    """Create word pairs"""
    blog_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    word_name = models.CharField(max_length=50)
    word_translation = models.CharField(max_length=50)
    word_note = models.CharField(max_length=100)
    
    def __str__(self):
        return self.word_name