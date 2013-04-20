from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import admin

admin.autodiscover()
admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.unregister(Group)


# Basic URL
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)


# Seat
urlpatterns += patterns('seat.views',
	url(r'^$', 'index'),
	url(r'^about$', 'about'),
	url(r'^seat/(?P<id>\d+)/?$', 'seat'),
)