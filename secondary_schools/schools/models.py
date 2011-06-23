from django.db import models
from django.contrib.auth.models import User
from iceland.models import Municipality
#from secondary_schools.student_housing.models import Housing
#from community.models import Album

#class SchoolAlbum(Album):
#	school = models.ForeignKey('School')

class School(models.Model):
	name = models.CharField(max_length=256)
	identity_number = models.CharField(max_length=10)
	abbreviation = models.CharField(max_length=4)
	address = models.CharField(max_length=128)
	municipality = models.ForeignKey(Municipality)
	telephone = models.CharField(max_length=7)
	fax = models.CharField(max_length=7, null=True, blank=True)
	email = models.EmailField()
	website = models.URLField()
	#principal = models.ForeignKey(User)
	#description = models.TextField(blank=True, null=True)
	#municipality = models.CharField(max_length=128, blank=True)
	#student_housing = models.ForeignKey('Housing', blank=True, null=True)
	#logo = models.ImageField(upload_to='schools/logos', blank=True, null=True)
	#representative_photo = models.ImageField(upload_to='schools/photos', 
	#					 blank=True, null=True)
	#introductory_video = models.FileField(upload_to='schools/videos', 
	#				      blank=True, null=True)

	def __unicode__(self):
		return self.name

#class CurriculaInformation(models.Model):
#	school = models.ForeignKey(School)
#	activities = models.TextField(blank=True, null=True)
#	policy = models.TextField(blank=True, null=True)
#	administration = models.TextField(blank=True, null=True)
#	organization = models.TextField(blank=True, null=True)
#	instructional_methods = models.TextField(blank=True, null=True)
#	evaluation = models.TextField(blank=True, null=True)
#	support_measures = models.TextField(blank=True, null=True)
#	student_services = models.TextField(blank=True, null=True)
#	pupil_rights = models.TextField(blank=True, null=True)
#	cooperation = models.TextField(blank=True, null=True)
#	quality_control = models.TextField(blank=True, null=True)
#	national_curriculum = models.TextField(blank=True, null=True)
#	other_information = models.TextField(blank=True, null=True)

#	def __unicode__(self):
#		return 'Curricula information for', self.school
