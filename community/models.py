# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from site_structure.utils import slugicefy

class Article(models.Model):
	title = models.CharField('titill', max_length=256)
	slug = models.CharField(max_length=256, editable=False)
	content = models.TextField('innihald')
	author = models.ForeignKey(User, editable=False)
	published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugicefy(self.title)
		super(Article, self).save(*args, **kwargs)

	class Meta:
		unique_together = ('title', 'author')


class Album(models.Model):
	title = models.CharField(max_length=256)
	slug = models.SlugField(max_length=256, editable=False)
	description = models.TextField()
	creator = models.ForeignKey(User, editable=False)
	created = models.DateTimeField(auto_now=True)
	published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugicefy(self.title)
		super(Album, self).save(*args, **kwargs)

class Photo(models.Model):
	title = models.CharField(max_length=256)
	slug = models.SlugField(max_length=256, editable=False)
	image = models.ImageField(upload_to='community/photos')
	album = models.ForeignKey(Album)
	uploader = models.ForeignKey(User, editable=False)
	published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugicefy(self.title)
		super(Photo, self).save(*args, **kwargs)

class Bookmark(models.Model):
	title = models.CharField('titill', max_length=256)
	slug = models.SlugField(max_length=256, editable=False)
	target_url = models.URLField('vefslóð')
	thumbnail = models.URLField(editable=False)
	description = models.TextField('Lýsing', blank=True, null=True)
	creator = models.ForeignKey(User, editable=False)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugicefy(self.title)
		super(Bookmark, self).save(*args, **kwargs)
