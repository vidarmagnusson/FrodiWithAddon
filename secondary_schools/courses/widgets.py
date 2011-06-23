from django import forms  # as forms
from django.forms.widgets import flatatt
# from django.forms.util import smart_unicode
from django.utils.html import escape
from django.utils.simplejson import JSONEncoder


class JQueryAutoCompleteMulti(forms.Textarea):
	def __init__(self, source, options={}, attrs={}):
		"""source can be a list containing the autocomplete values or a
		string containing the url used for the XHR request.
        
		For available options see the autocomplete sample page::
		http://jquery.bassistance.de/autocomplete/"""
        
		self.options = None
		self.attrs = {'autocomplete': 'off'}
		self.source = source
		if len(options) > 0:
			self.options = JSONEncoder().encode(options)
        
		self.attrs.update(attrs)
    
	def render_js(self, field_id):
		if isinstance(self.source, list):
			source = JSONEncoder().encode(self.source)
		elif isinstance(self.source, str):
			source = "'%s'" % escape(self.source)
		else:
			raise ValueError('source type is not valid')
        
		options = ''
		if self.options:
			options += ',%s' % self.options

		return u'$(\'#%s\').tokenInput(%s%s);' % (field_id, source, options)

	def render(self, name, value=None, attrs=None):
		final_attrs = self.build_attrs(attrs, name=name)
		if value:
			final_attrs['value'] = escape(value) # smart_unicode(value))

		if not self.attrs.has_key('id'):
			final_attrs['id'] = 'id_%s' % name    
        
		return u"""<textarea %(attrs)s></textarea>
		<script type="text/javascript"><!--//
		%(js)s//--></script>
		""" % {
			'attrs' : flatatt(final_attrs),
			'js' : self.render_js(final_attrs['id']),
		}	


class JQueryAutoComplete(forms.TextInput):
	def __init__(self, source, options={}, attrs={}):
		"""source can be a list containing the autocomplete values or a
		string containing the url used for the XHR request.
        
		For available options see the autocomplete sample page::
		http://jquery.bassistance.de/autocomplete/"""
        
		self.options = None
		self.attrs = {'autocomplete': 'off'}
		self.source = source
		if len(options) > 0:
			self.options = JSONEncoder().encode(options)
        
		self.attrs.update(attrs)
    
	def render_js(self, field_id):
		if isinstance(self.source, list):
			source = JSONEncoder().encode(self.source)
		elif isinstance(self.source, str):
			source = "'%s'" % escape(self.source)
		else:
			raise ValueError('source type is not valid')
        
		options = ''
		if self.options:
			options += ',%s' % self.options

		return u'$(\'#%s\').tokenInput(%s%s);' % (field_id, source, options)

	def render(self, name, value=None, attrs=None):
		final_attrs = self.build_attrs(attrs, name=name)
		if value:
			final_attrs['value'] = escape(value) # smart_unicode(value))

		if not self.attrs.has_key('id'):
			final_attrs['id'] = 'id_%s' % name    
        
		return u'''<input type="text" %(attrs)s/>
		<script type="text/javascript"><!--//
		%(js)s//--></script>
		''' % {
			'attrs' : flatatt(final_attrs),
			'js' : self.render_js(final_attrs['id']),
		}


class BulletEntry(forms.Textarea):
	def __init__(self, attrs=None):
		self.attrs = {}
		pass

	def render(self, name, value=None, attrs=None):
		return u""" 
		<textarea id=\"id_%(name)s\" style=\"display: none;\"></textarea>
		<ul>
		    <li><input id="%(name)s_newbullet"/></li>
		</ul>
		<script>
	    var idno_%(name)s = 0;
	    $("#%(name)s_newbullet").keyup(function(event) {
	        if (event.keyCode == '13') {
	            event.preventDefault();
	            idno_%(name)s++;
	            $("#%(name)s_newbullet").parent().before("<li id=\\"%(name)s_bullet_" + idno_%(name)s + "\\">" + $("#%(name)s_newbullet").val() + " <span class=\\"bullet_delete\\" onclick=\\"$('#%(name)s_bullet_" + idno_%(name)s + "').remove();\\">x</span></li>");
				$("#id_%(name)s");
	            $("#%(name)s_newbullet").val("");
	        }
	    });
	    $("#%(name)s_newbullet").keypress(function(event) { if(event.keyCode == '13') { event.preventDefault(); } });
		</script>
		""" % { "attrs": flatatt(self.attrs), "name": name}
