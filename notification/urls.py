from django.conf.urls import patterns, url
from notification import views

urlpatterns = patterns('',
        url(r'^login/$', views.user_login, name='login'),
        url(r'^home/$', views.home, name='home'),
        url(r'^$', views.index, name='index'),
       
        )