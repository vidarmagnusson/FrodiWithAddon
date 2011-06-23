from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.cache import cache_page
from secondary_schools.courses.models import *
import simplejson as json


def autocomplete_topics(request):
	if not request.GET.get('q'):
		return HttpResponse(mimetype='text/plain')
    
	q = request.GET.get('q')
	limit = request.GET.get('limit', 15)
	try:
		limit = int(limit)
	except ValueError:
		return HttpResponseBadRequest() 

	topics = Topic.objects.filter(name__startswith=q)[:limit]
	subs = []
	for s in subjects:
		subs.append({"id": s.id, "name": s.name})
	return HttpResponse(json.dumps(subs), mimetype='application/json')

# autocomplete_topics = cache_page(autocomplete_topics, 60)

def get_subjectabbrev(request):
	if not request.GET.get('q'):
		return HtppResponse(mimetype='text/plain')

	q = request.GET.get('q')
	limit = request.GET.get('limit', 15)
        try:
                limit = int(limit)
        except ValueError:
                return HttpResponseBadRequest()

        subjects = SubjectCombination.objects.filter(name__startswith=q)[:limit]
        subs = []
        for s in subjects:
                subs.append({"id": s.id, "name": s.name})
        return HttpResponse(json.dumps(subs), mimetype='application/json')


def autocomplete_subjects(request):
	if not request.GET.get('q'):
		return HttpResponse(mimetype='text/plain')
    
	q = request.GET.get('q')
	limit = request.GET.get('limit', 15)
	try:
		limit = int(limit)
	except ValueError:
		return HttpResponseBadRequest() 

	subjects = Subject.objects.filter(name__startswith=q)[:limit]
	subs = []
	for s in subjects:
		subs.append({"id": s.id, "name": s.name})
	return HttpResponse(json.dumps(subs), mimetype='application/json')


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
