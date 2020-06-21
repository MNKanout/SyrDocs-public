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
    # Select source Language
    source_language = forms.TypedChoiceField(choices=languages, label='',
    widget=(forms.Select(attrs={'class':'form-control mb-3'})))

    # Select output langauge
    target_language = forms.TypedChoiceField(choices=languages, label='',
    widget=(forms.Select(attrs={'class':'form-control mb-3'})))

    # Input text field
    input_langauge = forms.CharField(max_length=50, label='',
        widget=forms.TextInput(attrs={'placeholder':'Translate text',
                    'class':'form-control mb-3'}))

    # Translation output field
    result = forms.CharField(label='', 
        widget=forms.Textarea(attrs={'placeholder':'Translation','class':'form-control mb-3'}))