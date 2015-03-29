from django import forms
from collection.models import Collection
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions 

class CollectionForm(forms.ModelForm):
	'''def __init__(self, *args, **kwargs):
		super(CollectionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'collectionForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit'
'''
		#self.helper.add_input(Submit('submit', 'Submit'))
	#collection = forms.ModelChoiceField(queryset=Collection.objects.all(), widget=forms.HiddenInput())
	class Meta:
		model = Collection
		fields = ('collection_description', 'collection_name')
		exclude = ('author',)

	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.layout = Layout(
		Field('collection_name', css_class='input-xlarge'),
		Field('collection_description', rows="3", css_class='input-xlarge'),
		FormActions(
			Submit('save_changes', 'Save changes', css_class="btn-primary"),
			
		)
	) 
