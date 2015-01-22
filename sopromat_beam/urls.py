from django.conf.urls import patterns, url

from sopromat_beam import views

urlpatterns = patterns('',# define app specific urls here, name and views.asd corresponds with func from views.py
    url(r'^/$', views.beam, name='index'),#main page
    url(r'^/tester/$', views.beam_tester, name='tester'),#tester page
    #url(r'^/tester/(?P<id>\d+)/$', views.beam_tester_get_task, name='tester_get_task'),#specific  task page
    url(r'^/stats/student', views.beam_stats_student, name='stats_student'),
    url(r'^/stats/teacher', views.beam_stats_teacher, name='stats_teacher'),
    url(r'^/tasks/$', views.beam_tasks, name='tasks'),
)

#name - по нему можно вызвать из хтмл кода