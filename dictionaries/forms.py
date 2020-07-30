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
                {'placeholder':'Word',
                'class':'form-control mt-1',
                'autocomplete':'off'
                }),

                'word_translation':forms.TextInput(attrs=
                {'placeholder':'Translation',
                'class':'form-control mt-1',
                'autocomplete':'off'
                }),
            }

languages = ( 
    ('ar', "Arabic"), 
    ('en', "English"), 
    ('no', "Norwegian"), 
    ('fr', "Frensh"), 
    ('sv', "Swedish"), 
)

class Translateform(forms.Form):
    """A simple translation form"""
    # Select source Language
    source_language = forms.TypedChoiceField(choices=languages, label='',initial='test initial',
    widget=(forms.Select(attrs={
        'class':'form-control',
        })))

    # Select output langauge
    target_language = forms.TypedChoiceField(choices=languages, label='',
    widget=(forms.Select(attrs={
        'class':'form-control',
        })))

    # Input text field
    input_langauge = forms.CharField(max_length=50, label='',
        widget=forms.TextInput(attrs={
            'placeholder':'Text',
            'class':'form-control',
            'autocomplete':'off',
            }))
    output_langauge = forms.CharField(max_length=50, label='',required=False,
        widget=forms.TextInput(attrs={
            'placeholder':'Translation',
            'class':'form-control',
            'autocomplete':'off',
            }))