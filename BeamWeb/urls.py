from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    url(r'^sopromat/', include('sopromat.urls', namespace="sopromat")),
    url(r'^sopromat/beam', include('sopromat_beam.urls', namespace="sopromat_beam")),
    url(r'^sopromat/stretch', include('sopromat_stretch.urls', namespace="sopromat_stretch")),
    url(r'^sopromat/twist', include('sopromat_twist.urls', namespace="sopromat_twist")),
    url(r'^sopromat/inertia', include('sopromat_inertia.urls', namespace="sopromat_inertia")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('myauth.urls', namespace="myauth")),
    url(r'^$', 'homepage.views.index'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
'''
в этом файле жанга смотрит где искать обработчиков ссылок этого проекта
1 строка - ссылки формата ww.website.ru/sopromat/ обрабатываются аппом sopromat, ссылки описаны в sopromat.urls
'''