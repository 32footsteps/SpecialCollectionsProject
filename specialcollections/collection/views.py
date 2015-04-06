from django.core.urlresolvers import reverse
from collection.models import Collection
from collection.forms import CollectionForm
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect


def index_view(request):
	collections = Collection.objects.filter(author=request.user)
	return render(request, 'collections/index.html', {'collections': collections})

def create_collection(request):

	if request.method == 'POST':
		form = CollectionForm(request.POST)
		user = request.user
		print(str(user.username))

		if form.is_valid():
			collection = form.save(commit=False)
			collection.author = user
			collection.save()
			messages.add_message(request, messages.INFO, 'Collection Created')
			return HttpResponseRedirect(reverse('collections:index'))

	else:
		form = CollectionForm()

	return render(request, 'collections/createcollection.html', {'form': form})

def get_collection(request, **kwargs):
	print(request)
	collection = Collection.objects.get(title=kwargs.get('collection', ''))
	print("collection " + str(collection.title))

	if request.user == collection.object.author:
		if request.method == 'GET':
			return render(request, 'collections/collection.html', {'collection': collection})