from django.forms import ModelForm
from secondary_schools.programmes.models import Programme

class ProgrammeForm(ModelForm):
	class Meta:
		model = Programme
