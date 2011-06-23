
from django import forms
from secondary_schools.courses.models import *
from secondary_schools.courses.widgets import *

class NewCourseForm(forms.ModelForm):
	class Meta:
		model = Course
		widgets = {
			"topics": JQueryAutoComplete("/programmes/courses/auto/topics/", {"multiple": True, "autoFill": True}),
			"subjects": JQueryAutoComplete("/programmes/courses/auto/subjects/", {"multiple": True, "autoFill": True}),
			"prerequisites": JQueryAutoCompleteMulti("/programmes/courses/auto/courses/", {"multiple": True, "autoFill": True, "multipleSeparator": " "}),
			"goals": BulletEntry(),
		}


class NewSubjectForm(forms.ModelForm):
	class Meta:
		model = SubjectCombination


class NewTopicForm(forms.ModelForm):
	class Meta:
		model = TopicCombination
