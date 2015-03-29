from django import forms
from collection_item.models import Item


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item

		fields = ('title', 'subject', 'description', 'publisher', 'contributor',
		 	'item_type', 'item_format', 'identifier', 'source', 'language', 
		 	'relation', 'coverage', 'rights', 'item_image')