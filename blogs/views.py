#Builtin modules
from django.shortcuts import render, redirect
from  django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404

# Poject modules
from .models import BlogPost
from .forms import BlogPostform
from dictionaries.models import Dictionary
from dictionaries.forms import Dictionaryform
from dictionaries.views import run_quickstart

def check_owner(request,blog):
    """Check the owner of the blog post"""
    if blog.owner != request.user:
        raise Http404

def index(request):
    """Showing the homepage"""
    return render(request,'blogs/index.html')

@login_required
def blog_posts(request,):
    """Show all blog posts"""
    if request.GET.get('newest'):
        blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
        user = request.user
        context = {'blogs':blogs,'user':user}
        return render(request,'blogs/blog_posts.html',context)

    elif request.GET.get('oldest'):
        blogs = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
        user = request.user
        context = {'blogs':blogs,'user':user}
        return render(request,'blogs/blog_posts.html',context)

    else:
        blogs = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
        user = request.user
        context = {'blogs':blogs,'user':user}
        return render(request,'blogs/blog_posts.html',context)

@login_required
def blog_post(request,post_pk):
    "Show blog post"
    # Blog post section
    blog_post = get_object_or_404(BlogPost,pk=post_pk)
    check_owner(request,blog_post)

    # Dictionary form section
    if request.method != 'POST':
        form = Dictionaryform()
    else:
        form = Dictionaryform(data=request.POST)
        if form.is_valid():
            new_dict = form.save(commit=False)
            new_dict.blog_post = blog_post
            new_dict.owner = request.user
            new_dict.save()
    dictionaries = blog_post.dictionary_set.filter(owner=request.user).order_by('word_name')

    # Translations section
    translation = run_quickstart()
    itext = translation['input']
    ttext = translation['translatedText']
    context = {'blog_post':blog_post,'post_pk':post_pk,'form':form,'dictionaries':dictionaries,'itext':itext,'ttext':ttext,'translation':translation}
    return render(request,'blogs/blog_post.html',context)

@login_required
def new_blog(request):
    """Show a page for entering a new blog post """
    if request.method !='POST':
        form = BlogPostform()
    else:
        form = BlogPostform(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blog_posts')
    #Display a blank form
    context = {'form':form}
    return render(request,'blogs/new_blog.html',context)

@login_required()
def edit_blog(request,blog_id):
    """Editing existing blog posts"""
    blog_post = BlogPost.objects.get(id=blog_id)
    check_owner(request,blog_post)
    if request.method != 'POST':
        form = BlogPostform(instance=blog_post)

    else:   #POST
        form = BlogPostform(instance=blog_post,data=request.POST)
        if request.POST.get('edit'): # Save and return to posts page.
            if form.is_valid():
                form.save()
                return redirect('blogs:blog_posts')

        elif request.POST.get('del'):# Delete selected post.
            blog_post.delete()
            return redirect('blogs:blog_posts')
        
        elif request.POST.get('save'): # Save changes
            if form.is_valid():
                form.save()

    #Display an empty page
    context = {'form':form,'blog_id':blog_id,'blog_post':blog_post}
    return render(request,'blogs/edit_blog.html',context)



@login_required
def del_post(request,blog_id):
    """Delete a spesifc post"""
    blog_post = BlogPost.objects.get(id=blog_id)
    check_owner(request,blog_post)
    if request.method != 'POST':
        form = BlogPostform(instance=blog_post)
    else:
        form = BlogPostform(instance=blog_post,data=request.POST)
        blog_post.delete()
        return redirect('blogs:blog_posts')
    #Display an empty page
    context = {'form':form,'blog_id':blog_id,'blog_post':blog_post}
    return render(request,'blogs/del_post.html',context)