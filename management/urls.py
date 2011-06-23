from django.conf.urls.defaults import *
from django.contrib import admin
from feedzilla.settings import *

admin.autodiscover()

urlpatterns = patterns('',
	url('^efnislausar-sidur/$', 'management.views.list_empty'),
	url('^nytt-efni(?P<url>/.*)', 'management.views.create_flatpage', name='modify-page'),
	url('^hlidarreitir/$', 'management.views.create_highlight'),
	url('^myndir-i-haus/$', 'management.views.header_images'),
	url('^myndir-i-haus/eyda(?P<url>/.*)$', 'management.views.delete_header_image'),
)
