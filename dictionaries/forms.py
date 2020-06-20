from django import forms
from django.db import models
from .models import Dictionary

class Dictionaryform(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ['word_name','word_translation']
        labels = {'word_name':'','word_translation':''}
        widgets = {
            'word_name':forms.TextInput(attrs=
            {'placeholder':'Add word'}),
            'word_translation':forms.TextInput(attrs={'placeholder':'Add meaning'})
        }

languages = ( 
    (1, "Arabic"), 
    (2, "English"), 
    (3, "Norwegian"), 
    (4, "Frensh"), 
    (5, "Swedish"), 
) 
class Translateform(forms.Form):
    """A simple translation form"""
    source_language = forms.TypedChoiceField(choices=languages,label='')
    target_language = forms.TypedChoiceField(choices=languages,label='')
    result = forms.CharField(widget=forms.Textarea())