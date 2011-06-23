# -*- encoding: utf-8 -*-
from django.template.defaultfilters import slugify

def slugicefy(value):
	value = value.replace(u'þ','th')
	value = value.replace(u'Þ','Th')
	value = value.replace(u'æ','ae')
	value = value.replace(u'Æ','Ae')
	value = value.replace(u'ð','d')
	value = value.replace(u'Ð','D')
	return slugify(value)

