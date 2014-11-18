from django.conf.urls import patterns, url

from cf_users import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
    url(r'^results/$', views.results, name='results'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^(?P<user_id>\d+)/edit_user/$', views.edit_user, name='edit_user'),
    url(r'^(?P<user_id>\d+)/edit_results/$', views.edit_results, name='edit_results'),
    url(r'^(?P<user_id>\d+)/delete_user/$', views.delete_user, name='delete_user'),
)
