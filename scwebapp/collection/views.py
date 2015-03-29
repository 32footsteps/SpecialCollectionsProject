from django.shortcuts import render
from collection.models import Collection


def index_view(request):
	print("collection index view")
	collections = Collection.objects.all()
	return render(request, 'collection/dashmain.html', {'collections':collections})