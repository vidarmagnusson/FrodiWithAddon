
from django.contrib import admin
from secondary_schools.courses.models import *

for a in [Subject, Topic, SubjectCombination, TopicCombination]:
	admin.site.register(a)

class CourseAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

admin.site.register(Course, CourseAdmin)
