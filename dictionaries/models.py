from django.db import models
from django.contrib.auth.models import User

class Dictionary(models.Model):
    """Create word pairs"""
    word_name = models.CharField(max_length=50)
    word_translation = models.CharField(max_length=50)
    word_note = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
