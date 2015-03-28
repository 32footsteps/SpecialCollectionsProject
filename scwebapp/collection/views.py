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
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAuthorOfCollection(),)

#perform_create hook makes user associated with request author of Collection
def perform_create(self, serializer):
	instance = serializer.save(author=self.request.user)

	return super(CollectionViewSet, self).perform_create(serializer)

#gets list of Collections associated with specific SCUser
class SCUserCollectionViewSet(viewsets.ViewSet):
	queryset = Collection.objects.select_related('author').all()
	serializer_class = CollectionSerializer

	def list(self, request, account_username=None):
		queryset = self.queryset.filter(author__username=account_username)
		serializer = self.serializer_class(queryset, many=True)

		return Response(serializer.data)