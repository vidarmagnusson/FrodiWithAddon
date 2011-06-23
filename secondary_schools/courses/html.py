# -*- coding: utf-8 -*-
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

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from site_structure.models import *
from secondary_schools.courses.models import *
from secondary_schools.courses.forms import *
import simplejson as json
import re

def index(request):
	ctx = {}
	courses = Course.objects.all().order_by('name')
	#courses = courses.filter(status=2)
	
	ctx["inprogress"] = courses

	return render_to_response("secondary_schools/courses/index.html", 
				  ctx, RequestContext(request))


#@login_required
def new_course(request):

	ctx = {'title':'Nýr áfangi'}

	if request.method == "POST":
		subjects = [Subject.objects.get_or_create(name=x.strip())[0] 
			for x in request.POST.get('subjects', '').split(',') 
			if x.strip() != '']

		#if len(subjects) > 0:
		#	subject = subjectcombination_find_by_set(subjects)
		#	if subject is None:
				# We need to ask questions.
		#		subject = SubjectCombination()
		#		subject.abbreviation = "???"
		#		abb = None
		#		if len(subjects) == 1:
		#			abb = subjects[0].name[:3].upper()
		#		elif len(subjects) == 2:
		#			abb = subjects[0].name[:2].upper() + subjects[1].name[:1].upper()
		#		elif len(subjects) == 3:
		#			abb = subjects[0].name[:1].upper() + subjects[1].name[:1].upper() + subjects[2].name[:1].upper()

		#		if abb is not None and subject_abbreviation_free(abb):
		#			subject.abbreviation = abb
		#		
		#		subject.save()
		#		subject.combination = subjects
		#		subject.save()
		#		ctx["newsubject"] = True
		#		ctx["newsubjectform"] = NewSubjectForm(subject)
		#	ctx["subject"] = subject

		topics = [Topic.objects.get_or_create(name=x.strip(), subject=subjects)[0] 
			for x in request.POST.get('topics', '').split(',') 
			if x.strip() != '']
		
		#if len(topics) > 0:
		#	topic = topiccombination_find_by_set(topics, subject)
			
		#	if topic is None:
		#		topic = TopicCombination()
		#		topic.abbreviation = "??"
		#		abb = None
		#		if len(topics) == 1:
		#			abb = topics[0].name[:2].upper()
		#		elif len(topics) == 2:
		#			abb = topics[0].name[:1].upper() + topics[1].name[:1].upper()

		#		if abb is not None and topic_abbreviation_free(abb):
		#			topic.abbreviation = abb
				
		#		topic.save()
		#		topic.combination = topics
		#		topic.save()
		#		ctx["newtopic"] = True
		#		ctx["newtopicform"] = NewTopicForm(topic)
		
		qdict = dict(request.POST)
		#qdict["subjects"] = [subjects.id]
		#qdict["topics"] = [topics.id]
		for x in qdict:
			qdict[x] = qdict[x][0]
		
		print qdict

		form = NewCourseForm(qdict)
		#print form
		#if form.is_valid():
		#	course = form.save(commit=False)
		#	course.author = request.user
		#	course.save()
		#	ctx["newcourse"] = course
		return HttpResponse('Tókst að vista. Þetta kemur svona ljótt því við erum bara að prófa innslátt.', mimetype="text/plain")
		#/nam-og-skolar/framhaldsskolar/namskrargrunnur/minir-afangar/')		
	#else:
	#	form = NewCourseForm()
		
	#ctx["form"] = form
	return render_to_response("secondary_schools/courses/newcourse.html", 
				  ctx, RequestContext(request))


#@login_required
def search(request):
	ctx = {}
	return render_to_response("secondary_schools/courses/search.html", ctx, RequestContext(request))

#@login_required
def course_info(request, courseid):
	ctx = {}
	try:
		if re.match('^\d', courseid):
			ctx['course'] = Course.objects.get(id=courseid)
		else:
			ctx['course'] = Course.objects.get(name=courseid)
	except:
		ctx['object'] = "Áfangi"
		return render_to_response("notfound.html", ctx, 
					  RequestContext(request))

	return render_to_response("secondary_schools/courses/course_info.html", ctx,
				  RequestContext(request))

