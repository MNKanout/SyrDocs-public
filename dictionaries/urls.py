from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'dictionaries'

urlpatterns = [
    # Embedded dictionary
    path('<int:post_pk>/',views.dictionary,name='dictionary'),
    # Delete a dictionary
    path('delete/<int:<blog_post_id>/<int:word_id>/',views.delete,name='delete'),
]