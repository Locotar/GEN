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
    url(r'^user/', include('login.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),  
)
