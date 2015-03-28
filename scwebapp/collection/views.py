import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from django.template import loader
from django.http import HttpResponse
from collection.permissions import IsAuthorOfCollection
from collection.models import Collection
from collection.serializers import CollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
	queryset = Collection.objects.order_by('-created_at')
	serializer_class = CollectionSerializer

	def get_permissions(self):
		if self.request.method in