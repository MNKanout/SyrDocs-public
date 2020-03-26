from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Show a page to register new users"""
    if request.method != 'POST':
        form = UserCreationForm
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect('blogs:index')
    #Display a blank form or an invalid form
    context = {'form':form}
    return render(request,'registration/register.html',context)


