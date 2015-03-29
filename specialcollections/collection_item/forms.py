from django import forms
from collection_item.models import Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions 

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('title', 'subject', 'description', 'publisher',
					'contributor', 'item_type', 'item_format', 
					'identifier', 'source', 'language', 'relation',
					'coverage', 'rights', 'item_image')
		exclude = ('creator', 'date')

	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.layout = Layout(
		Field('title', css_class='input-xlarge'),
		Field('subject', css_class='input-xlarge'),
		Field('description', rows="3", css_class='input-xlarge'),
		Field('publisher', css_class='input-xlarge'),
		Field('contributor', css_class='input-xlarge'),
		Field('item_type', css_class='input-xlarge'),
		Field('item_format', css_class='input-xlarge'),
		Field('identifier', css_class='input-xlarge'),
		Field('source', css_class='input-xlarge'),
		Field('language', css_class='input-xlarge'),
		Field('relation', css_class='input-xlarge'),
		Field('coverage', css_class='input-xlarge'),
		Field('rights', css_class='input-xlarge'),
		Field('item_image', css_class='input-xlarge'),


		FormActions(
			Submit('save', 'Save changes', css_class="btn-primary"),
			
		)
	) 
