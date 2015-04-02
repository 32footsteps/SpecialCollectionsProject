import datetime
from haystack import indexes
from collection_item.models import Item

class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    subject = indexes.CharField(model_attr='subject')
    description = indexes.CharField(model_attr='description')
    publisher = indexes.CharField(model_attr='publisher')
    contributor = indexes.CharField(model_attr='contributor')
    item_type = indexes.CharField(model_attr='item_type')
    item_format = indexes.CharField(model_attr='item_format')
    identifier = indexes.CharField(model_attr='identifier')
    source = indexes.CharField(model_attr='source')
    language = indexes.CharField(model_attr='language')
    relation = indexes.CharField(model_attr='relation')
    coverage = indexes.CharField(model_attr='coverage')

    def get_model(self):
    	return Item

    def index_queryset(self, using=None):
    	"""Used when the entire index for model is updated"""
    	return self.get_model().objects.all()
