from django.conf.urls import patterns, url

from sopromat import views

urlpatterns = patterns('',# define app specific urls here, name and views.asd corresponds with func from views.py
    url(r'^$', views.index, name='index'),
)

#EVERY CLASS OF TASKS SHOULD BE A SEPARATE APP