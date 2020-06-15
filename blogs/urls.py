from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    #The home page
    path('',views.index,name='index'),
    #Page for showing all blog posts
    path('blog_posts/',views.blog_posts,name='blog_posts'),
    # Page for a specific post
    path('blog_post/<int:post_pk>/',views.blog_post,name='blog_post'),
    #Page for adding new blog posts
    path('new_blog/',views.new_blog,name='new_blog'),
    #Page for editing existing blog posts
    path('edit_blog/<int:blog_id>/',views.edit_blog,name='edit_blog'),
    #Page for deleting posts
    path('del_post/<int:blog_id>/',views.del_post,name='del_post'),



]