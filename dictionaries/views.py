#Django modules
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth. decorators import login_required
from django.http import Http404
#Third party modules
from google.cloud import translate_v2 as translate
#Project modules
from .models import Dictionary
from .forms import Dictionaryform
from blogs.models import BlogPost

def check_owner(request,dictionary):
    """Check the owner of the dictionary"""
    if request.user != dictionary.owner_id:
        raise Http404


@login_required
def dictionary(request,post_pk):
    """Display a form for entering a new dictionary"""
    blog_post = get_object_or_404(BlogPost,pk=post_pk)
    dict_form = Dictionaryform(data=request.POST)
    if dict_form.is_valid():
        new_dict = dict_form.save(commit=False)
        # Set to which post does the dictionary belonge to.
        new_dict.blog_post = blog_post
        # Set the owner of the new dictionary.
        new_dict.owner_id = request.user
        new_dict.save()
        return redirect('blogs:blog_post',post_pk)
    
@login_required
def delete(request,blog_post_id,word_id):
    """Delete an existed dictionary"""
    dictionary = get_object_or_404(Dictionary,pk=word_id)
    check_owner(request,dictionary)
    if request.method == 'POST':
        form = Dictionaryform(instance=dictionary,data=request.POST)
        dictionary.delete()
        return redirect('blogs:blog_post', blog_post_id)

def translate_(request):
    dict_form = Dictionaryform(request.POST)
    if dict_form.is_valid():
        source_language = dict_form.cleaned_data['source_language']
        target_language = dict_form.cleaned_data['target_language']
        input_langauge = dict_form.cleaned_data['text']
        # Set new defaults
        request.session['source_language'] = source_language
        request.session['target_language'] = target_language
        # Set translation client
        translate_client = translate.Client()

    # The text to translate
        text = str(input_langauge)
        if source_language == target_language:
            translation = 'Invalid language option!'
            return translation
        else:
            translation = translate_client.translate(text,source_language=source_language,
            target_language=target_language)
            return translation['translatedText']
