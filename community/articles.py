# -*- encoding: utf-8 -*-
from site_structure.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect

from community.models import Article
from community.forms import ArticleForm

import markdown
import re

@login_required
def new(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			new_article = form.save(commit=False)
			new_article.author = request.user
			new_article.content = markdown.markdown(new_article.content)
			new_article.save()

		return HttpResponseRedirect('/samfelag/minar-sidur/')
	
	return render('community/new.html', {'title': 'Ný grein', 'form':ArticleForm(),}, request)

def all(request):
	ctx = {'title': 'Greinasafn'}
	articles = Article.objects.all().order_by('-published')
	
	collection = []
	for article in articles:		
		summary = re.sub('(<.*?>)*','',article.content)[:250]
		if len(article.content) > 250:
			summary = '%s...' % summary
		#collection.append({'title':article.title,'url':reverse('article', kwargs={'user':user,'slug':article.slug}), 'summary':summary})	
		collection.append({'title':article.title, 'url':reverse('view-article', kwargs={'user':article.author,'slug':article.slug}), 'published':article.published, 'summary':summary, 'author':article.author})	
	
	ctx['articles'] = collection

	return render('community/articles.html', ctx, request)

def mine(request, username=None):
	ctx = {'title': 'Greinasafn %s' % (username)}
	if not username:
		if request.user.is_authenticated():
			username = request.user.username
			ctx['title'] = 'Mitt greinasafn'
		else: 
			raise Http404

	articles = Article.objects.filter(author__username=username).order_by('-published')
	
	collection = []
	for article in articles:
		
		summary = re.sub('(<.*?>)*','',article.content)[:250]
		if len(article.content) > 250:
			summary = '%s...' % summary
		#collection.append({'title':article.title,'url':reverse('article', kwargs={'user':user,'slug':article.slug}), 'summary':summary})	
		collection.append({'title':article.title, 'url':reverse('view-article', kwargs={'user':username,'slug':article.slug}), 'published':article.published, 'summary':summary, 'author':article.author})	
	
	ctx['articles'] = collection

	return render('community/articles.html', ctx, request)

def view(request, user, slug):
	try:
		article = Article.objects.filter(author__username=user).get(slug=slug)
	except:
		raise Article.DoesNotExist

	return render('community/article.html', {'article':article}, request)
