"""
URL configuration for lmcx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from events.views.list_view import EventListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EventListView.as_view(template_name='home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('events/', include('events.urls')),
    path('announcements/', include('announcements.urls')),
    # All of these urls are placeholders to get the Navbar working.
    path('results/', TemplateView.as_view(template_name='base.html'), name='results'),
    path('photos/', TemplateView.as_view(template_name='base.html'), name='photos'),
    path('sponsors/', TemplateView.as_view(template_name='base.html'), name='sponsors'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
