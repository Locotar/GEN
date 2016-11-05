from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # url(r'^$' , 'learn.views.index'),
    # url(r'^$', 'learn.views.index', name='home'),
    url(r'^$', include('login.urls')),
    # user
    url(r'^login/', include('login.urls')),
    # url(r'^main/', include('main.urls')),

    url(r'^env/', include('env.urls')),
    url(r'^suite/', include('suite.urls')),
    url(r'^task/', include('task.urls')),
    url(r'^queue/', include('queue.urls')),
    url(r'^usermanage/', include('usermanage.urls')),

    url(r'^getEnvFromDB/', include('getEnvFromDB.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # css js image  -> folder
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),  
)
