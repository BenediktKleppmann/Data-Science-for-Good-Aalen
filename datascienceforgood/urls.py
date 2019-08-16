from django.contrib import admin
from collection import views
from django.views.generic import RedirectView
from django.conf.urls import include, url
from django.urls import path


urlpatterns = [

    # ==================================================
    # THE WEBSITE  
    # ==================================================
    url(r'^$', views.home, name='home'),
    url(r'^analyse_12_09_2019/$', views.analyse_12_09_2019, name='analyse_12_09_2019'),
    url(r'^analyse_26_09_2019/$', views.analyse_26_09_2019, name='analyse_26_09_2019'),
    url(r'^analyse_10_10_2019/$', views.analyse_10_10_2019, name='analyse_10_10_2019'),
    url(r'^leute/$', views.leute, name='leute'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^test_page/$', views.test_page, name='test_page'),
]