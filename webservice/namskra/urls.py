from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('webservice.namskra',
	(r'^framhaldsskolar/namsgreinar', 'framhaldsskolar.get_subjects'),
	(r'^framhaldsskolar/subjects/autocomplete', 'framhaldsskolar.autocomplete_subjects'),
	(r'^framhaldsskolar/namsgrein/skammstofun/(?P<abbreviation>[^/]*)', 'framhaldsskolar.get_subject_by_abbreviation'),
	(r'^framhaldsskolar/subjects/(?P<subjects>[^/]*)', 'framhaldsskolar.get_subject'),

	(r'^framhaldsskolar/topics/autocomplete', 'framhaldsskolar.autocomplete_topics'),
	(r'^framhaldsskolar/topics/(?P<topics>[^/]*)', 'framhaldsskolar.get_topic'),
	(r'^framhaldsskolar/vidfangsefni/skammstofun/(?P<subject>[^/]*)/(?P<abbreviation>[^/]*)', 'framhaldsskolar.get_topic_by_abbreviation'),
)
