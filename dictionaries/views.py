#Django modules
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth. decorators import login_required
from django.http import Http404
#Third party modules
from google.cloud import translate_v2 as translate
#Project modules
from .models import Dictionary
from .forms import Dictionaryform, Translateform

def check_owner(request,dictionary):
    """Check the owner of the dictionary"""
    if request.user != dictionary.owner:
        raise Http404

@login_required
def del_dictionary(request,blog_post_id,word_id):
    """Delete an existed dictionary"""
    dictionary = get_object_or_404(Dictionary,pk=word_id)
    check_owner(request,dictionary)
    if request.method == 'POST':
        form = Dictionaryform(instance=dictionary,data=request.POST)
        dictionary.delete()
        return redirect('blogs:blog_post', blog_post_id)

def run_quickstart():
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = u'Hello, world!'
    # The target language
    target = 'ru'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    return translation
    #print(u'Text: {}'.format(text))
    #print(u'Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]