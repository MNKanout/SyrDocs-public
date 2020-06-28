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
from blogs.models import BlogPost

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

@login_required
def show_dictionaries(request,blog_post):
    """Return all user's dictionaries related to a spesifc post"""
    dictionaries = blog_post.dictionary_set.filter(owner=request.user).order_by('word_name')
    return dictionaries

@login_required
def dictionary_form(request,blog_post,post_pk):
    """Display a form for entering a new dictionary"""
    dict_form = Dictionaryform(data=request.POST)
    if dict_form.is_valid():
        new_dict = dict_form.save(commit=False)
        # Set to which post does the dictionary relate to.
        new_dict.blog_post = blog_post
        # Set the owner of the new dictionary.
        new_dict.owner = request.user
        new_dict.save()
        # Return to the same post after saving the new dictionary.


def translate_text(input_language,source_language,target_language):
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = str(input_language)
    if source_language == target_language:
        translation = 'Invalid language option!'
        return translation
        # Translates
    else:
        translation = translate_client.translate(text,source_language=source_language,
            target_language=target_language)
        return translation['translatedText']