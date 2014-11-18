from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'', include('cf_users.urls', namespace="cf_users")),
    url(r'^admin/', include(admin.site.urls)),
)
