from django.template import RequestContext
from site_structure.shortcuts import render

def index(request):
	return render_to_response('frodi.html', {}, request)
