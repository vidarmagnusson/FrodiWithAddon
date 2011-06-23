# -*- coding: utf-8 -*-

#from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
#from dynamic_content.models import Content
#from dynamic_content.models import Image

def rss(request):
	return render_to_response('rss/rss.html', {},
                                  context_instance=RequestContext(request))

#def content(request):
#	path = request.get_full_path()

#	ctxt = {'title':'Vefurinn er í vinnslu',
#		'content':'Unnið er að því að koma efninu á vefinn',
#		'path':path}

#	content = Content.objects.filter(path__exact=path)

#	if content:
#		if content[0].name: ctxt['title'] = content[0].name
#		if content[0].content: ctxt['content'] = content[0].html

#	return render_to_response('content.html', ctxt,
#				  context_instance=RequestContext(request))

#@csrf_protect
#def edit(request, path):
#	try:
#		content = Content.objects.get(path__exact=path)
#	except Content.DoesNotExist:
#		return render_to_response('notfound.html', {},
#					  context_instance=RequestContext(request))
#
#	if request.POST:
#	        content.content = request.POST['content']
#       	content.save()
#        	return HttpResponseRedirect(content.path)
#	else:
#        	return render_to_response('edit.html', locals(),
#					  context_instance=RequestContext(request))

#def images(request):
#	ctxt = {'album':[]}
#	for img in Image.objects.all():
#		if img.image.height < img.image.width: 
#			position = 'center'
#		else: 
#			position = 'right'
#
#		ctxt['album'].append({'name':img.name, 
#				      'path':img.image.url,
#				      'position':position})
#
#	return render_to_response('myndir.html', ctxt,
#				  context_instance=RequestContext(request))
