# Curriculum - Web application for creating and managing educational curricula
# Copyright (C) 2010  The Ministry of Education, Science and Culture, Iceland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from secondary_schools.models import *

class Subject(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

    def save(self):
        self.name = self.name.lower()
        super(Subject, self).save()

    class Meta:
        verbose_name = _('subject')
        verbose_name_plural = _('subjects')

class SubjectCombination(models.Model):
	combination = models.ManyToManyField(Subject)
	abbreviation = models.CharField(max_length=4)
	def __unicode__(self):
		return "%s - %s" % (self.abbreviation, self.subjects())

	def subjects_list(self):
		return [x.name for x in self.combination.all()]
		
	def subjects(self):
		return ", ".join(self.subjects_list())
        
	class Meta:
		verbose_name = _('subject combination')
		verbose_name_plural = _('subjects combinations')

class Topic(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

    def save(self):
        self.name = self.name.lower()
        super(Topic, self).save()

    class Meta:
        verbose_name = _('topic')
        verbose_name_plural = _('topics')

class TopicCombination(models.Model):
    combination = models.ManyToManyField(Topic)
    subject = models.ForeignKey(SubjectCombination)
    abbreviation = models.CharField(max_length=2)
    def __unicode__(self):
        return "%s - %s" % (self.abbreviation, self.topics())

    def topics_list(self):
        return [x.name for x in self.combination.all()]
    
    def topics(self):
        return ", ".join(self.topics_list())

    class Meta:
        verbose_name = _('topic combination')
        verbose_name_plural = _('topics combinations')

def subjectcombination_find_by_set(subjects):
	possible = SubjectCombination.objects.filter(combination__in=subjects)
	for p in possible:
		if set(p.combination.all()) == set(subjects):
			return p
	return None

def topiccombination_find_by_set(topics, subject):
	possible = TopicCombination.objects.filter(combination__in=topics)
	for p in possible:
		if set(p.combination.all()) == set(topics):
			return p
	return None

def subject_abbreviation_free(abbr):
	a = SubjectCombination.objects.filter(abbreviation=abbr)
	if len(a) > 0:
		return False
	return True

def topic_abbreviation_free(abbr):
	a = TopicCombination.objects.filter(abbreviation=abbr)
	if len(a) > 0:
		return False
	return True

class Course(models.Model):
    STATUS_CHOICES = ( 
			(1, _('Draft')),
			(2, _('Ready for review')),
			(3, _('School Accepted')),
			(4, _('Government Accepted')), 
		)

    LEVEL_CHOICES = (
			(1, _('Level 1')),
			(2, _('Level 2')),
			(3, _('Level 3')),
			(4, _('Level 4')),
		 )

    descriptive_name = models.CharField(max_length=255)
    subjects = models.ForeignKey(SubjectCombination)
    topics = models.ForeignKey(TopicCombination)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    credits = models.IntegerField()
    description = models.TextField()

    status = models.IntegerField(choices=STATUS_CHOICES, 
                                 editable=False, default=0)

    modification_date = models.DateTimeField(default=datetime.now, 
                                             editable=False)

    # history = link to another course or none 

    prerequisites = models.TextField()

    author = models.ForeignKey(User, editable=False)

    name = models.CharField(max_length=9, blank=True, editable=False)
    version = models.IntegerField(default=-1, editable=False)

    def __unicode__(self):
        return self.name
        
    def id_name(self):
        return '%s.%s' % (self.name, self.version)

    def save(self):
        self.name = '%s%s%s%s' % (
                self.subjects.abbreviation,
                self.level,
                self.topics.abbreviation,
                '%02d' % self.credits,
                )
        super(Course, self).save()

    def update_prerequisites_rules(self):
        pass

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')

class Goal(models.Model):
	course		= models.ForeignKey(Course)
	goal		= models.CharField(max_length=300)

class Evaluation(models.Model):
	goal		= models.ForeignKey(Goal)
	evaluation	= models.TextField()
