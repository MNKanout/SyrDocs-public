from django.db import models
from django.contrib.auth.models import User

from blogs.models import BlogPost

class Dictionary(models.Model):
    """Create word pairs"""
    blog_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    word_name = models.CharField(max_length=50)
    word_translation = models.CharField(max_length=50)
    word_note = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name_plural = 'dictionaries'
    
    def __str__(self):
        """Return a sting representation of the model"""
        return self.word_name