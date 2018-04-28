from django.conf.urls import patterns, url
from usermanage import views
 
urlpatterns = patterns('',
                       url(r'^usermanage/', views.usermanage, name='usermanage'),
                       # show all users
                       url(r'^$', views.usermanage, name='usermanage'),
                       url(r'^ShowUser/$', views.ShowUser, name='ShowUser'),
                       url(r'^AddUser/$', views.AddUser, name='AddUser'),
                       # url(r'^Warning/$', views.Warning, name='Warning'),
                       url(r'^DelUser/$', views.DelUser, name='DelUser'),
                       url(r'^CheckUser/$', views.CheckUser, name='CheckUser'),
                       url(r'^ModUser/$', views.ModUser, name='ModUser'),
                       url(r'^ShowUserHTMLTemplate/$', views.ShowUserHTMLTemplate, name='ShowUserHTMLTemplate'),
                       )
