# Curriculum - Web application for creating and managing educational curricula
# Copyright (C) 2010  The Ministry of Education, Science and Culture, Iceland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('secondary_schools.courses',
	(r'^$', 'html.index'),        
	(r'^minir-afangar/$', 'html.index'),
        (r'^listi-yfir-afanga/$', 'html.index'),
	(r'^nyr-afangi/$', 'html.new_course'),
	#(r'^search/$', 'html.search'),
	#(r'^info/(?P<courseid>\d+|\w{3}\d\w{2}\d{2}\S{4})/$', 'html.course_info'),
	
	#(r'^auto/topics/$', 'json.autocomplete_topics'),
	(r'^auto/subjects/$', 'json.autocomplete_subjects'),
	#(r'^auto/courses/$', 'json.autocomplete_courses'),
)
