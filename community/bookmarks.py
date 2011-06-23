# -*- encoding: utf-8 -*-
from site_structure.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect

from community.models import Bookmark
from community.forms import BookmarkForm

import markdown
import re

@login_required
def new(request):
	if request.method == 'POST':
		form = BookmarkForm(request.POST)
		if form.is_valid():
			new_bookmark = form.save(commit=False)
			new_bookmark.creator = request.user
			new_bookmark.save()

		return HttpResponseRedirect('/samfelag/minar-sidur/')
	
	return render('community/new.html', {'title': 'Bæta við tengli', 'form':BookmarkForm(),}, request)

def all(request):
	ctx = {'title': 'Tenglasafn'}
	bookmarks = Bookmark.objects.all().order_by('-created')
	
	collection = []
	for bookmark in bookmarks:		
		collection.append({'title':bookmark.title, 'url':bookmark.target_url, 'published':bookmark.created, 'summary':bookmark.description, 'author':bookmark.creator})	
	
	ctx['content'] = collection

	return render('community/content_list.html', ctx, request)

def mine(request, username=None):
	ctx = {'title': 'Tenglasafn %s' % (username)}
	if not username:
		if request.user.is_authenticated():
			username = request.user.username
			ctx['title'] = 'Mitt tenglasafn'
		else: 
			raise Http404

	bookmarks = Bookmark.objects.filter(creator__username=username).order_by('-created')
	
	collection = []
	for bookmark in bookmarks:
		collection.append({'title':bookmark.title, 'url':bookmark.target_url, 'published':bookmark.created, 'summary':bookmark.description, 'author':bookmark.creator})	
	
	ctx['content'] = collection

	return render('community/content_list.html', ctx, request)

def view(request, user, slug):
	try:
		article = Article.objects.filter(author__username=user).get(slug=slug)
	except:
		raise Article.DoesNotExist

	return render('community/article.html', {'article':article}, request)
