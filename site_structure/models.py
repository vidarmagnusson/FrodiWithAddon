from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.contrib.sites.managers import CurrentSiteManager
from site_structure.utils import slugicefy


class Menu(models.Model):
	title = models.CharField(max_length=128)
	slug = models.SlugField(editable=False)
	url = models.CharField(max_length=255, blank=True)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
	order = models.IntegerField(blank=True, null=True)
	sites = models.ManyToManyField(Site)
	groups = models.ManyToManyField(Group, blank=True, null=True)
	objects = models.Manager()
	on_site = CurrentSiteManager(field_name='sites')
	
	def __unicode__(self):
		#if self.parent:
			#return ' - '*(self.url.count('/')-1) + ': '.join([self.parent.title, self.title])
		
		return ' - '*(self.url.count('/')-1) + self.title

	def save(self, *args, **kwargs):
		self.slug = slugicefy(self.title)

		flatpage = None
		try:
			flatpage = FlatPage.objects.get(url=self.url)
		except:
			pass
		
		if self.parent:
			self.url = '/'.join([self.parent.url[:-1], self.slug, ''])
		else:
			self.url = '/'

		if flatpage:
			flatpage.url = self.url
			flatpage.save()

		super(Menu, self).save(*args, **kwargs)

		for child in self.children.all():
			child.save()

	class Meta:
		unique_together = (('url', 'title'),)
		ordering = ('url', 'order', 'title')

class Header(models.Model):
	image = models.ImageField(upload_to='hausmyndir')
	sites = models.ManyToManyField(Site)
	objects = models.Manager()
	on_site = CurrentSiteManager(field_name='sites')
	
	def __unicode__(self):
		return self.image.name

class Highlight(models.Model):
        title = models.CharField(max_length=128)
        link = models.CharField(max_length=128)
	icon = models.ImageField(upload_to='highlight_icons', blank=True, null=True)
        order = models.IntegerField()
        pages = models.ManyToManyField('Menu', blank=False, related_name='highlights')

	def __unicode__(self):
                return self.title

        class Meta:
                ordering = ('title', 'order')

