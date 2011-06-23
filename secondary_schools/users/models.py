from django.db import models

from profiles.models import UserProfile
from secondary_schools.schools.models import School
from secondary_schools.courses.models import Subject

class SecondarySchoolUser(models.Model):
	profile = models.ForeignKey(UserProfile, unique=True)
	school = models.ManyToMany(School)
