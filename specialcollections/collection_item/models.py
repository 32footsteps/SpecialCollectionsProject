from django.db import models
from django.core.files.base import ContentFile
from collection_user.models import SCUser

class Item(models.Model):
	title = models.CharField(max_length=120, unique=True)
	creator = models.CharField(max_length=30, blank=False) #models.ForeignKey(SCUser) 
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
	is_approved = models.BooleanField(default=False)

	item_image = models.ImageField(upload_to='media/')


	def __str__(self):
		return self.title

class TempItem(models.Model):
	temp_item = models.ForeignKey(Item)

	def __str__(self):
		return self.temp_item.title

