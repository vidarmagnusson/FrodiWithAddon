from django.db import models

class CountryArea(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField(blank=True, null=True)
	points = models.CommaSeparatedIntegerField(max_length=1024, blank=True, null=True)

	def __unicode__(self):
		return self.name

class Municipality(models.Model):
	postal_code = models.PositiveIntegerField()
	name = models.CharField(max_length=128)
	logo = models.ImageField(upload_to='iceland/municipalities/logos', blank=True, null=True)
	area = models.ForeignKey(CountryArea)

	def __unicode__(self):
		return '%d - %s' % (self.postal_code, self.name)
