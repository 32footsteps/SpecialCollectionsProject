from django import forms
from collection.models import Collection


class CollectionForm(forms.ModelForm):
	class Meta:
		model = Collection
		fields = ('collection_name', 'collection_description', 'item')