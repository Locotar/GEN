from django.conf.urls import patterns, url
from queue import views

 
urlpatterns = patterns('',
    url(r'^$', views.queue, name='queue'),
    url(r'^queue/$',views.queue,name = 'queue'),
)
