from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth. decorators import login_required
from django.http import Http404

from .models import Dictionary
from .forms import Dictionaryform

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