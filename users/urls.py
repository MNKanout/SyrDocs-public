"""Define url patterns for users"""
from django.urls import path, include
from django.contrib.auth import urls
from . import views

app_name = 'users'

urlpatterns = [
    #Include default auth urls.
    path('',include('django.contrib.auth.urls')),
    #Page to register new users
    path('register/',views.register,name='register'),

]