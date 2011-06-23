from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Example:
    # (r'^Frodi/', include('Frodi.foo.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^notendur/innskraning/$', login, {'template_name':'users/login.html'}),
    url(r'^notendur/utskraning/$', logout, {'template_name':'users/logout.html'}),
    #url(r'^myndir/$', 'dynamic_content.views.images'),
    #url(r'^breyta(?P<path>/.*)$', 'dynamic_content.views.edit'),
    url(r'^samfelag/', include('community.urls')),
    url(r'^namskrargrunnur/framhaldsskolar/', include('secondary_schools.courses.urls')),
    url(r'^stjornbord/', include('management.urls')),
    url(r'^api/', include('webservice.urls')),
    url(r'^nam-og-skolar/framhaldsskolar/', include('secondary_schools.urls')),
    url(r'^api/', include('webservice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/'}),
    #url(r"", 'site_structure.views.rss'),
    url('', include('feedzilla.urls')),
)
