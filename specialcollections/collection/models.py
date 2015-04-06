from django.db import models
from collection_user.models import SCUser
from collection_item.models import Item

class Collection(models.Model):
	'''class Meta:
		unique_together = (('collection_name', 'item'),)'''

	collection_name = models.CharField(max_length=70, primary_key=True)
	author = models.ForeignKey(SCUser, default=None, blank=False)

	collection_description = models.TextField()
	item = models.ManyToManyField(Item, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.collection_name

