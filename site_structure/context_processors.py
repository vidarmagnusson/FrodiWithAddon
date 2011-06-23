from site_structure.models import Menu, Highlight, Header
from django.contrib.sites.models import Site
import random

def populate_menu(menu, crumbs, request):
	url = request.get_full_path()

	# Check whether we should really add this to the list based
	# on user groups and allowed groups (no groups selected means
	# everybody should be able to se
	user = request.user
	groups = menu.groups.all()

	if (not len(groups)) or set(user.groups.all()) & set(groups):
		selected = url.startswith(menu.url)
		menudict = {'title':menu.title, 'url':menu.url,
			    'status':('active' if selected else 'inactive'),
			    'children':[child for child in [populate_menu(c,crumbs,request) for c in menu.children.all().order_by('order')] if child != None]}
	
		if selected: crumbs.insert(0, menudict)
		return menudict

def generate_menu(request):
	try:
		root = Menu.on_site.get(url__exact='/')
	except Menu.DoesNotExist:
		return None

	crumbs = []
	# The ignore is a dictionary of everything
	# ...but how populate_menu populates crumbs is the interesting part
	ignore = populate_menu(root, crumbs, request)
	return {'crumbs':crumbs}

def random_header(request):
	headers = Header.on_site.all()
	try:
		header = random.choice(headers).image.url
	except IndexError:
		header = ''
	
	return {'header_img':header}

def generate_highlights(request):
	path = request.get_full_path()
	
        try:
		menu = Menu.objects.get(url__exact=path)
        except Menu.DoesNotExist:
                return {'highlights':None}

	return {'highlights':menu.highlights.all().order_by('order')}
