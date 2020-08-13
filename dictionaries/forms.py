from django import forms
from django.db import models
from .models import Dictionary

languages = ( 
    ('ar', "Arabic"), 
    ('en', "English"), 
    ('no', "Norwegian"), 
    ('fr', "Frensh"), 
    ('sv', "Swedish"), 
)

class Dictionaryform(forms.ModelForm):
    """New keywords adding form """
    source_language = forms.TypedChoiceField(choices=languages, label='',
    widget=(forms.Select(attrs={
        'class':'form-control',
        })))
    
    target_language = forms.TypedChoiceField(choices=languages, label='',
    widget=(forms.Select(attrs={
        'class':'form-control',
        })))

    class Meta:
        model = Dictionary
        fields = ['text','translation']
        labels = {'text':'','translation':''}
        widgets = {
                    'text':forms.TextInput(attrs=
                    {'placeholder':'Text',
                    'class':'form-control',
                    'autocomplete':'off'
                    }),

                    'translation':forms.TextInput(attrs=
                    {'placeholder':'Translation',
                    'class':'form-control',
                    'autocomplete':'off',
                    }),
                }