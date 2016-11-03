from django.conf.urls import patterns, url
from suite import views

 
urlpatterns = patterns('',
    url(r'^$', views.suite, name='suite'),
    url(r'^suite/$',views.suite,name = 'suite'),
)
