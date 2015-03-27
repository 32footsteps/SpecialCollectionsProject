from django.db import models
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


		item_image = models.ImageField(upload_to='items')

		def __str__(self):
			return self.title