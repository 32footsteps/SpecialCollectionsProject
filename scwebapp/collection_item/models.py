from django.db import models
from django.core.files.base import ContentFile
from collection_user.models import SCUser

class Item(models.Model):
	title = models.CharField(max_length=120, unique=True)
	creator = models.ForeignKey(SCUser) #models.CharField(max_length=80, blank=False)
	subject = models.CharField(max_length=120, blank=False)
	description = models.TextField()
	publisher = models.CharField(max_length=80, blank=False)
	contributor = models.CharField(max_length=80, blank=False)
	date = models.DateTimeField(auto_now_add=True)
	item_type = models.CharField(max_length=80, blank=True)
	item_format = models.CharField(max_length=20, blank=False)
	identifier = models.CharField(max_length=40, blank=False)
	source = models.CharField(max_length=40, blank=False)
	language = models.CharField(max_length=40, blank=False)
	relation = models.CharField(max_length=40, blank=False)
	coverage = models.CharField(max_length=80, blank=True)
	rights = models.CharField(max_length=80, blank=True)

	updated_at = models.DateTimeField(auto_now=True)


	item_image = models.ImageField(upload_to='media/')

	def create_item(self, title, **kwargs):
		if not title:
			raise ValueError('Valid Title Required')

		if not kwargs.get('subject'):
			raise ValueError('Valid Subject Required')

		if not kwargs.get('description'):
			raise ValueError('Valid Description Required')

		if not kwargs.get('publisher'):
			raise ValueError('Valid Publisher Required')

		item_file_content = ContentFile(str(title))
		item = Item()
		item.save

	def __str__(self):
		return self.title

class TempItem(models.Model):
	temp_item = models.ForeignKey(Item)

	def __str__(self):
		return self.temp_item.title

