from django.conf.urls import patterns, url
from task import views

 
urlpatterns = patterns('',
    url(r'^$', views.task, name='task'),
    url(r'^task/$',views.task,name = 'task'),
)
