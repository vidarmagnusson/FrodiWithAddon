from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.cache import cache_page
from secondary_schools.courses.models import *
import simplejson as json

def get_topic_by_abbreviation(request,subject,abbreviation):
	subjectu = subject.upper()
	topic = abbreviation.upper()

	try:
		topic_combination = TopicCombination.objects.get(abbreviation__exact=topic, subject__abbreviation__exact=subjectu)
		return HttpResponse(json.dumps({'id':topic_combination.id,
						'abbreviation':topic_combination.abbreviation,
						'subject':topic_combination.subject.abbreviation,
						'topic':topic_combination.topics()}), mimetype='application/json')
	except:
		return HttpResponse(json.dumps({}), mimetype='application/json')

def get_subject_by_abbreviation(request,abbreviation):
        q = abbreviation.upper()

	try:
	        subject = SubjectCombination.objects.get(abbreviation__exact=q)
		return HttpResponse(json.dumps({'id':subject.id,
						'abbreviation':subject.abbreviation,
						'subject':subject.subjects()}), mimetype='text/plain')
	except SubjectCombination.DoesNotExist:
		return HttpResponse(json.dumps({}), mimetype='application/json')


def get_topics(request):
        if not request.GET.get('q'):
                return HttpResponse(mimetype='text/plain')

        q = request.GET.get('q')
        limit = request.GET.get('limit', 15)

        try:
                limit = int(limit)
        except ValueError:
                return HttpResponseBadRequest()

        topics = Topic.objects.filter(name__startswith=q.lower())[:limit]
        subs = []
        for t in topics:
                for tc in t.topiccombination_set.all():
                        subs.append({"id":tc.id,
                                     "name":tc.topics(),
                                     "abbreviation":tc.abbreviation})
        return HttpResponse(json.dumps(subs), mimetype='application/json')

def get_topic(request,topics):
	
	# Split topics into 
	topic_list = [x.strip(' ') for x in topics.split(',')]	
	topic_list[-1:] = topic_list[-1].split(' og ')

	tops = {}
	tid = []
	topexist = []

	# Mark topics that exist (if use requires emphasis)
	for topic in topic_list:
		try:
			t = Topic.objects.get(name__exact=topic.lower())
			tid.append(t)
			topexist.append({'id':t.id,
					 'name':t.name,
					 'exists':True})
		except Topic.DoesNotExist:
			topexist.append({'name':topic.capitalize(),
					 'exists':False})

	tops['topics'] = topexist
			
	if len(tid) == len(topic_list):
		tcs = TopicCombination.objects.filter(combination__id=tid[0].id)
		for tc in tcs:
			if set(tc.combination.all()) == set(tid):
				tops['abbr'] = tc.abbreviation

	return HttpResponse(json.dumps(tops), mimetype='text/plain')

def get_subject(request,subjects):
	
	subject_list = [x.strip(' ') for x in subjects.split(',')]
	subject_list[-1:] = subject_list[-1].split(' og ')
	
	subs = {}

	sid = []
	subexist = []
	for subject in subject_list:
		try:
			s = Subject.objects.get(name__exact=subject.lower())
			sid.append(s)
			subexist.append({'id':s.id,
					 'name':s.name, 
					 'exists':True})
		except Subject.DoesNotExist:
			subexist.append({'name':subject.capitalize(), 
					 'exists':False})

	subs['subjects'] = subexist

	if len(sid) == len(subject_list):
		scs = SubjectCombination.objects.filter(combination__id=sid[0].id)
		for sc in scs:
			if set(sc.combination.all()) == set(sid):
				subs['abbr'] = sc.abbreviation
				
	return HttpResponse(json.dumps(subs), mimetype='text/plain')

def get_subjects(request):
	if not request.GET.get('q'):
		return HttpResponse(mimetype='text/plain')

	q = request.GET.get('q')
	limit = request.GET.get('limit', 15)

        try:
                limit = int(limit)
        except ValueError:
                return HttpResponseBadRequest()

	subjects = Subject.objects.filter(name__startswith=q.lower())[:limit]
        subs = []
        for s in subjects:
		for sc in s.subjectcombination_set.all():
	                subs.append({"id":sc.id,
				     "name":sc.subjects(),
				     "abbreviation":sc.abbreviation})
        return HttpResponse(json.dumps(subs), mimetype='application/json')

def autocomplete_subjects(request):
	if not request.GET.get('term'):
		return HttpResponse(mimetype='text/plain')

	q = request.GET.get('term').split(',')[-1].strip(' ')
	if q:
		subjects = Subject.objects.filter(name__startswith=q.lower())
        	subs = []
        	for s in subjects:
			subs.append(s.name)
	        return HttpResponse(json.dumps(subs), mimetype='application/json')
	else:
		return HttpResponse(mimetype='text/plain')

def autocomplete_topics(request):
        if not request.GET.get('term'):
                return HttpResponse(mimetype='text/plain')

        q = request.GET.get('term').split(',')[-1].strip(' ')
        if q:
                topics = Topic.objects.filter(name__startswith=q.lower())
                subs = []
                for t in topics:
                        subs.append(t.name)
                return HttpResponse(json.dumps(subs), mimetype='application/json')
        else:
                return HttpResponse(mimetype='text/plain')

def autocomplete_courses(request):
	if not request.GET.get('q'):
		return HttpResponse(mimetype='text/plain')
    
	q = request.GET.get('q')
	limit = request.GET.get('limit', 15)
	try:
		limit = int(limit)
	except ValueError:
		return HttpResponseBadRequest() 

	courses = Course.objects.filter(name__startswith=q)[:limit]
	subs = []
	for s in subjects:
		subs.append({"id": s.id, "name": s.name})
	return HttpResponse(json.dumps(subs), mimetype='application/json')
