from django.conf.urls import patterns, url
from GetPizza import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
