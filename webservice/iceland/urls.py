from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('webservice.iceland',
	(r'^kort/merkja/(?P<area>[^/]*)/$', 'map.mark'),
)
