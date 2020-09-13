"""lastVer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sites import requests
from django.urls import path, include
from lastVer.core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('singup/', views.singup, name='singup'),
    path('admin/', admin.site.urls),
    path('swf/',views.showfile ,name='showfile'),
    #path('upload/', views.upload.as_view(), name='upload2')
    path('Docs/', views.Docs_list, name='Docs_list'),
    path('Docs/upload/', views.upload_Docs, name='upload_Docs'),
    path('Docs/<int:pk>', views.delete_Docs, name='delete_Docs'),
    path('todo', views.todo, name='todo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
