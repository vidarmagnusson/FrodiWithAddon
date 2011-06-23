from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^namskra/', include('webservice.namskra.urls')),
	(r'^island/', include('webservice.iceland.urls')),
)

