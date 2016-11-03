from django.conf.urls import patterns, url
from env import views

 
urlpatterns = patterns('',
    url(r'^$', views.env, name='env'),
    url(r'^env/$',views.env,name = 'env'),
)
