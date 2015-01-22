from django.conf.urls import patterns, url

from sopromat_inertia import views

urlpatterns = patterns('',# define app specific urls here, name and views.asd corresponds with func from views.py
    url(r'^/$', views.inertia_tester, name='tester'),)

#name - по нему можно вызвать из хтмл кода