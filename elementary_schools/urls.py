from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^skolar/$', 'elementary_schools.views.index'),
	url(r'^skolar/(?P<school>[^/]*)/$', 'elementary_schools.views.school_info'),
)

