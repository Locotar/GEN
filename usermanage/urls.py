from django.conf.urls import patterns, url
from usermanage import views


 
urlpatterns = patterns('',
    url(r'^$', views.usermanage, name='usermanage'),
    url(r'^usermanage/',views.usermanage,name = 'usermanage'),
    url(r'^regist/$',views.regist,name = 'regist'),
)
