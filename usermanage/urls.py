from django.conf.urls import patterns, url
from usermanage import views
 
urlpatterns = patterns('',
    url(r'^$', views.usermanage, name='usermanage'),
    # show all users
    url(r'^usermanage/',views.usermanage,name = 'usermanage'),
    url(r'^ShowUser/$',views.ShowUser,name = 'ShowUser'),
    url(r'^AddUser/$',views.AddUser,name = 'AddUser'),
    url(r'^DelUser/$',views.DelUser,name = 'DelUser'),
)
