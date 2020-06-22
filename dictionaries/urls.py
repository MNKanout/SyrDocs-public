from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'dictionaries'

urlpatterns = [
    # Embedded dictionary
    path('dictionary/<int:post_pk>/',views.dictionary_form,name='dictionary_form'),
    # Delete a dictionary
    path('del_dictionary/<int:<blog_post_id>/<int:word_id>/',views.del_dictionary,name='del_dictionary'),
]