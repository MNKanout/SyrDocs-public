from django.shortcuts import render, redirect
from  django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostform

def check_blog_owner(request,blog):
    if blog.owner != request.user:
        raise Http404

def index(request):
    """Showing the homepage"""
    return render(request,'blogs/index.html')

def blog_posts(request):
    """Show all blog posts"""
    blogs = BlogPost.objects.all()
    context = {'blogs':blogs}
    return render(request,'blogs/blog_posts.html',context)

@login_required
def new_blog(request):
    """Show a page for entering a new blog post """
    if request.method !='POST':
        form = BlogPostform()
    else:
        form = BlogPostform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_posts')
    #Display a blank form
    context = {'form':form}
    return render(request,'blogs/new_blog.html',context)

@login_required()
def edit_blog(request,blog_id):
    """Editing existing blog posts"""
    blog_post = BlogPost.objects.get(id=blog_id)
    check_blog_owner(request,blog_post)
    if request.method != 'POST':
        form = BlogPostform(instance=blog_post)
    else:
        form = BlogPostform(instance=blog_post,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_posts')
    #Display an empty page
    context = {'form':form,'blog_id':blog_id}
    return render(request,'blogs/edit_blog.html',context)

