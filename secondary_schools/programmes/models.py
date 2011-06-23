# -*- encoding: utf-8 -*-
from django.db import models
from secondary_schools.courses.models import Course

class ExamLevel(models.Model):
	LEVEL_CHOICES = (
			(1, '1. þrep'),
			(2, '2. þrep'),
			(3, '3. þrep'),
			(4, '4. þrep'),
		)

	level = models.PositiveIntegerField('Þrep', choices=LEVEL_CHOICES)	

	min_ratio_level_one = models.PositiveIntegerField('Minnsta hlutfall á fyrsta þrepi')
	max_ratio_level_one = models.PositiveIntegerField('Mesta hlutfall á fyrsta þrepi')

	min_ratio_level_two = models.PositiveIntegerField('Minnsta hlutfall á öðru þrepi', blank=True, null=True)
	max_ratio_level_two = models.PositiveIntegerField('Mesta hlutfall á öðru þrepi', blank=True, null=True)

	min_ratio_level_three = models.PositiveIntegerField('Minnsta hlutfall á þriðja þrepi', blank=True, null=True)
	max_ratio_level_three = models.PositiveIntegerField('Mesta hlutfall á þriðja þrepi', blank=True, null=True)

	min_ratio_level_four = models.PositiveIntegerField('Minnsta hlutfall á fjórða þrepi', blank=True, null=True)
	max_ratio_level_four = models.PositiveIntegerField('Mesta hlutfall á fjórða þrepi', blank=True, null=True)

	def __unicode__(self):
		return u'%d. þrep' % (self.level)	

class Exam(models.Model):
	title = models.CharField('Titill prófs', unique=True, max_length=128)
	description = models.TextField('Lýsing')
	level = models.ForeignKey(ExamLevel)

	minimum_credits = models.PositiveIntegerField('Lágmarkseiningar')
	maximum_credits = models.PositiveIntegerField('Hámarkseiningar')

	def __unicode__(self):
		return self.title

#class ExtraRule(models.Model):
#	title = models.CharField('Útskýring', max_length=256)
#	exam = models.ForeignKey(Exam)
#	subject = models.ManyToManyField(through='SubjectLevel')
#	minimum_credits = models.PositiveIntegerField('Lágmarkseiningafjöldi')

#class SubjectLevel(models.Model):
#	LEVEL_CHOICES = ((1, '1. þrep'),
#			 (2, '2. þrep'),
#			 (3, '3. þrep'),
#			 (4, '4. þrep'))
			 
#	subject = models.ForeignKey(SubjectCombination)
#	rule = models.ForeignKey(ExtraRule)
#	level = models.PositiveIntegerField(choices=LEVEL_CHOICES)

class CoursePackage(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField(blank=True, null=True)
	courses = models.ManyToManyField(Course)

class Programme(models.Model):

	title = models.CharField('titill', max_length=256)
	identity = models.CharField(max_length=10, editable=False)

	exam = models.ForeignKey(Exam)
	credits = models.IntegerField('einingar', null=True, blank=True)

	#field = models.CharField()
	description = models.TextField()
	goals = models.TextField()
	prerequisites = models.TextField()
	
	core = models.ForeignKey(CoursePackage, related_name='core_courses_set')
	specialization = models.ManyToManyField(CoursePackage, related_name='specializations_set')
	packaged_electives = models.ManyToManyField(CoursePackage, related_name='packaged_electives_set')
	free_electives = models.ForeignKey(CoursePackage, related_name='free_electives_set')

	created = models.DateTimeField(auto_now_add=True)

