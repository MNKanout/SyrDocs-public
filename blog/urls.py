from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Defualt urls 
    path('admin/', admin.site.urls),
    # Blog post app urls
    path('',include('blogs.urls')),
    # Dictionary app urls
    path('edit_dictionary/',include('dictionaries.urls')),
    # Users app urls
    path('users/',include('users.urls')),
    # Tinymce urls
    path('tinymce/', include('tinymce.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
