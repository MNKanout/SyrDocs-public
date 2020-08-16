from django import forms
from django.db import models
from .models import Dictionary

languages = ( 
    ("af", "Afrikaans"),
 	("sq", "Albanian"),
 	("ar", "Arabic"),	
	("hy", "Armenian"),
 	("az", "Azerbaijani"),
	("eu", "Basque"),
	("be", "Belarusian"),  	
	("bg", "Bulgarian"), 	 	
	("ca", "Catalan"),	
	("zh-CN", "Chinese (Simplified)"), 	
	("zh-TW", "Chinese (Traditional)"),	
 	("hr", "Croatian"), 	
 	("cs", "Czech"),		
 	("da", "Danish"), 	    
 	("nl", "Dutch"), 	
 	("en", "English"), 	
 	("et", "Estonian"),
 	("tl", "Filipino"),
 	("fi", "Finnish"),
 	("fr", "French"),
 	("gl", "Galician"),
 	("ka", "Georgian"),
 	("de", "German"),
 	("el", "Greek"),
 	("ht", "Haitian"),
 	("iw", "Hebrew"),
 	("hi", "Hindi"),
 	("hu", "Hungarian"),
 	("is", "Icelandic"),
 	("id", "Indonesian"),
 	("ga", "Irish"),
 	("it", "talian"),
 	("ja", "Japanese"),
 	("ko", "Korean"),
 	("lv", "Latvian"),
 	("lt", "Lithuanian"),
    ("mk", "Macedonian"),
 	("ms", "Malay"),
 	("mt", "Maltese"),
 	("no", "Norwegian"),
 	("fa", "Persian"),
 	("pl", "Polish"),
 	("pt", "Portuguese"),
 	("ro", "Romanian"),
 	("ru", "Russian"),
 	("sr", "Serbian"),
 	("sk", "Slovak"	),
 	("sl", "Slovenian"), 	
 	("es", "Spanish"),
 	("sw", "Swahili"),	
 	("sv", "Swedish"),	
 	("th", "Thai"),
 	("tr", "Turkish"),
 	("uk", "Ukrainian"),  	
 	("ur", "Urdu"),
 	("vi", "Vietnamese"), 	
 	("cy", "Welsh"),
 	("yi", "Yiddish"), 	
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