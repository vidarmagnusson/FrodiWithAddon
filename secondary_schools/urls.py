from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r'^$', 'site_structure.views.rss'),
	(r'^namskrargrunnur/framhaldsskolar/afangar/', include('secondary_schools.courses.urls')),
	(r'^namskrargrunnur/framhaldsskolar/brautir/', include('secondary_schools.programmes.urls')),
	(r'^skolar/', include('secondary_schools.schools.urls')),

        #(r'^namskrargrunnur/$', include(Frodi.secondary_schools.courses.urls)),
)

