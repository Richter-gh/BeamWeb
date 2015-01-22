from django.conf.urls import patterns, url

from sopromat_stretch import views

urlpatterns = patterns('',# define app specific urls here, name and views.asd corresponds with func from views.py
    url(r'^/$', views.stretch, name='index'),#main page
    url(r'^/tester/$', views.stretch_tester, name='tester'),#tester page
    #url(r'^/tester/(?P<id>\d+)/$', views.stretch_tester_get_task, name='tester_get_task'),#specific  task page
    url(r'^/stats/student', views.stretch_stats_student, name='stats_student'),
    url(r'^/stats/teacher', views.stretch_stats_teacher, name='stats_teacher'),
    url(r'^/tasks/$', views.stretch_tasks, name='tasks'),
)

#name - по нему можно вызвать из хтмл кода