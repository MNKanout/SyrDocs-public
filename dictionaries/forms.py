from django import forms
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