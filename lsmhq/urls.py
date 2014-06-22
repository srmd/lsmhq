from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('core.urls', namespace='core')),
    url(r'^django_admin/', include(admin.site.urls)),
)
