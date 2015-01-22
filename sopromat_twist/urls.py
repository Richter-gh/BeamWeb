from django.conf.urls import patterns, url

from sopromat_twist import views

urlpatterns = patterns('',# define app specific urls here, name and views.asd corresponds with func from views.py
    url(r'^/$', views.twist, name='index'),#main page
    url(r'^/tester/$', views.twist_tester, name='tester'),#tester page
    #url(r'^/tester/(?P<id>\d+)/$', views.twist_tester_get_task, name='tester_get_task'),#specific  task page
    url(r'^/stats/student', views.twist_stats_student, name='stats_student'),
    url(r'^/stats/teacher', views.twist_stats_teacher, name='stats_teacher'),
    url(r'^/tasks/$', views.twist_tasks, name='tasks'),
)

#name - по нему можно вызвать из хтмл кода