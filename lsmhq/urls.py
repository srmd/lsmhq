from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include('core.urls', namespace='admin')),
    url(r'^dj_admin/', include(admin.site.urls)),
)
