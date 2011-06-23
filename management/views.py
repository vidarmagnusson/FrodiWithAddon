# -*- encoding: utf-8 -*-
from django.contrib.flatpages.models import FlatPage
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve, reverse
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from site_structure.shortcuts import render
from site_structure.models import Menu, Header
from site_structure.forms import MenuForm, HighlightForm, PartialFlatPageForm
import markdown

@login_required
def list_empty(request):
	menu_items = Menu.on_site.all().order_by('url')
	empty = []
	for menu_item in menu_items:
		try:
			match = resolve(menu_item.url)
		except:	
			try:
				FlatPage.objects.get(url=menu_item.url)
			except:
				empty.append({'title':menu_item.title,
					      'url':reverse('modify-page', kwargs={'url':menu_item.url}),})

	return render('management/url_list.html', {'title':'Efnislausar síður' ,'list':empty}, request)

@login_required
def create_flatpage(request, url):
        if request.method == 'POST':
                form = PartialFlatPageForm(request.POST)
		page = form.save(commit=False)
		page.enable_comments = False
		page.registration_required = False
		page.content = markdown.markdown(page.content)
		page.url = url
		page.save()
		page.sites.add(Site.objects.get_current())
		form.save_m2m()

                return HttpResponseRedirect(url)
        
        return render('management/new.html', {'title':'Síðuskrif', 'form':PartialFlatPageForm(),}, request)

@login_required
def create_highlight(request):
        if request.method == 'POST':
                form = HighlightForm(request.POST)
		highlight = form.save(commit=False)
		highlight.order = 0
		highlight.save()
		form.save_m2m()
		
		try:
	                return HttpResponseRedirect(highligt.pages.all()[0])
		except:
			return HttpResponseRedirect('/')
        
        return render('management/new.html', {'title':'Nýr hliðarreitur', 'form':HighlightForm(),}, request)

@login_required
def header_images(request):
	headers = Header.objects.all()	
	return render('management/headers.html', {'title':'Myndir í haus', 'headers':headers}, request)


@login_required
def delete_header_image(request, url):

	header = None
		
	for h in Header.objects.all():
		if h.image.url == url:
			header = h

	if not header:
		return render('message.html', {'msg':'Mynd fannst ekki'}, request)

	if request.method == 'POST':
		header.delete()
		return render('message.html', {'msg':'Tókst að eyða mynd'}, request)
	else:
		return render('management/delete_header.html', {'header':header}, request)
