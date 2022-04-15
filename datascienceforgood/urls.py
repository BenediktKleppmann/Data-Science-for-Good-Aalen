"""datascienceforgood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^/$', views.home, name='home'),
    re_path(r'^feinstaub/$', views.feinstaub, name='feinstaub'),
    re_path(r'^landnutzung/$', views.landnutzung, name='landnutzung'),
    re_path(r'^analyse_10_10_2019/$', views.analyse_10_10_2019, name='analyse_10_10_2019'),
    re_path(r'^leute/$', views.leute, name='leute'),
    re_path(r'^kontakt/$', views.kontakt, name='kontakt'),
    re_path(r'^test_page/$', views.test_page, name='test_page'),
    path('admin/', admin.site.urls),
]
