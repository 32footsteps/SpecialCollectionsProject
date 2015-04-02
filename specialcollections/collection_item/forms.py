from django import forms
from collection_item.models import Item
from haystack.forms import ModelSearchForm, SearchForm
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
		Field('item_image', css_class='input-xlarge'),
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

		FormActions(
			Submit('save', 'Save changes', css_class="btn-primary"),
			
		)
	)
"""
class BasicItemSearchForm(SearchForm):

"""
class AdvancedItemSearchForm(ModelSearchForm):
	title = forms.CharField(max_length=80, required=True)
	subject = forms.CharField(max_length=120, required=True)
	description = forms.CharField(max_length=420, required=True)
	publisher = forms.CharField(max_length=80, required=True)
	contributor = forms.CharField(max_length=80, required=True)
	item_type = forms.CharField(max_length=80, required=False)
	item_format = forms.CharField(max_length=20, required=True)
	identifier = forms.CharField(max_length=40, required=True)
	source = forms.CharField(max_length=40, required=True)
	language = forms.CharField(max_length=40, required=True)
	relation = forms.CharField(max_length=40, required=True)
	coverage = forms.CharField(max_length=80, required=False)

	def search(self):
		sqs = super(AdvancedItemSearchForm, self).search()

		if not self.is_valid():
			return self.no_query_found()

		if self.is_valid() and self.cleaned_data['title']:
			sqs = sqs.filter(content = self.cleaned_data['title'])

		if self.is_valid() and self.cleaned_data['subject']:
			sqs = sqs.filter(content = self.cleaned_data['subject'])

		if self.is_valid() and self.cleaned_data['description']:
			sqs = sqs.filter(content = self.cleaned_data['description'])

		if self.is_valid() and self.cleaned_data['publisher']:
			sqs = sqs.filter(content = self.cleaned_data['publisher'])

		if self.is_valid() and self.cleaned_data['contributor']:
			sqs = sqs.filter(content = self.cleaned_data['contributor'])

		if self.is_valid() and self.cleaned_data['item_type']:
			sqs = sqs.filter(content = self.cleaned_data['item_type'])

		if self.is_valid() and self.cleaned_data['item_format']:
			sqs = sqs.filter(content = self.cleaned_data['item_format'])

		if self.is_valid() and self.cleaned_data['identifier']:
			sqs = sqs.filter(content = self.cleaned_data['identifier'])

		if self.is_valid() and self.cleaned_data['source']:
			sqs = sqs.filter(content = self.cleaned_data['source'])

		if self.is_valid() and self.cleaned_data['language']:
			sqs = sqs.filter(content = self.cleaned_data['language'])

		if self.is_valid() and self.cleaned_data['relation']:
			sqs = sqs.filter(content = self.cleaned_data['relation'])

		if self.is_valid() and self.cleaned_data['coverage']:
			sqs = sqs.filter(content = self.cleaned_data['coverage'])

		return sqs