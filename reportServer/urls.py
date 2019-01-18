from django.conf.urls import patterns, url
from reportServer import views

 
urlpatterns = patterns('',
    url(r'^$', views.reportServer, name='reportServer'),
    url(r'^reportServer/$',views.reportServer,name = 'reportServer'),
)
