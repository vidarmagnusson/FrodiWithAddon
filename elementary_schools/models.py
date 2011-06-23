from django.db import models
from iceland.models import Municipality
from site_structure.utils import slugicefy

class School(models.Model):
	name = models.CharField(unique=True, max_length=256)
	slug = models.SlugField(editable=False)
	official_name = models.CharField(max_length=256, blank=True, null=True)
        identity_number = models.CharField(max_length=10)
        address = models.CharField(max_length=128)
        municipality = models.ForeignKey(Municipality, related_name='elementary_school')
        telephone = models.CharField(max_length=7, blank=True, null=True)
        fax = models.CharField(max_length=7, null=True, blank=True)
        email = models.EmailField(null=True, blank=True)
	website = models.URLField(null=True, blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugicefy(self.name)
		super(School, self).save(*args, **kwargs)

	class Meta:
		ordering = ['name']
