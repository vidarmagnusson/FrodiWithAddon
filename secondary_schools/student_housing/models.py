from django.db import models
from community.models import Album

class Photo(models.Model):
	title = models.CharField(max_length=128)
	image = models.ImageField(upload_to='student_housing')
	album = models.ForeignKey(Album)

class RoomAlbum(Album):
	room = models.ForeignKey('RoomType')

class RoomType:
	size = CharField(max_length=16)
	description = TextField()
	monthly_cost = IntegerField()
	housing = models.ForeignKey(Housing)

class HousingAlbum(Album):
	housing = models.ForeignKey('Housing')

class Housing(models.Model):
	description = TextField()
	extra_information = models.URLField(blank=True, null=True)
	manager = models.CharField(max_length=256, blank=True, null=True)
	phone_number = models.CharField(max_length=7)

class PriceListEntry(models.Model)
	entry = models.CharField(max_length=256)
	footnote = models.CharField(max_length=256, blank=True, null=True)
	price = models.PositiveIntegerField()
	service = models.ForeignKey(Services, related_name='pricelist')

class Services(models.Model):
	title = models.CharField(max_length=256)
	description = models.TextField()

