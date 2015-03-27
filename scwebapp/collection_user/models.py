from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class SCUserManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('Valid Email Required')

		if not kwargs.get('username'):
			raise ValueError('Valid Username Required')

		if not kwargs.get('first_name'):
			raise ValueError('Valid First Name Required')

		if not kwargs.get('last_name'):
			raise ValueError('Valid Last Name Required')

		user = self.model(
			email=self.normalize_email(email), username=kwargs.get('username'), first_name=kwargs.get('first_name'),
			last_name=kwargs.get('last_name')
		)

		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, email, password, **kwargs):
		user = self.create_user(email, password, **kwargs)

		user.is_admin = True
		user.save()

		return user


class SCUser(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=50, unique=True)

	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)

	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = SCUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

	def __str__(self):
		return self.username

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])
