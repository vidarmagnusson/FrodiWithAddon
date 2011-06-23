from django.forms import ModelForm
from django.contrib.flatpages.models import FlatPage
from site_structure.models import Menu, Highlight

class FlatPageForm(ModelForm):
	class Meta:
		model = FlatPage

class PartialFlatPageForm(ModelForm):
	class Meta:
		model = FlatPage
		fields = ('title', 'content')

class HighlightForm(ModelForm):
	class Meta:
		model = Highlight
		fields = ('title', 'link', 'pages')
		
class MenuForm(ModelForm):
	class Meta:
		model = Menu
