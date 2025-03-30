"""
URL configuration for KitsuneCore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Add this for language selection
]

urlpatterns += i18n_patterns(
    # path('captain/', admin.site.urls),
    path('core/', include('apps.CoreApp.urls')),  
    # path('auth/', include('apps.AuthApp.urls')), 
    path('', include('apps.HomeApp.urls', namespace='HomeApp')),
    prefix_default_language=True,
)