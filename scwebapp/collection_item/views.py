from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from collection_item.models import Item
from collection_item.permissions import IsCreatorOfItem
from collection_item.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def create(self, request):
		print("serializer data: " + str(request.data))
		serializer = self.serializer_class(data=request.data)