from django.conf.urls import patterns, url
from getEnvFromDB import views

 
urlpatterns = patterns('',
    url(r'^$', views.getEnvFromDB, name='getEnvFromDB'),
    url(r'^getEnvFromDB/$',views.getEnvFromDB,name = 'getEnvFromDB'),
)
