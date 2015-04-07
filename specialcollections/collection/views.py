from django.core.urlresolvers import reverse
from collection.models import Collection
from collection.forms import CollectionForm
from collection_item.models import Item
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from haystack.query import SearchQuerySet

def index_view(request):
	collections = Collection.objects.filter(author=request.user)
	return render(request, 'collections/index.html', {'collections': collections})

def create_collection(request):

	if request.method == 'POST':
		form = CollectionForm(request.POST)
		user = request.user

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
	collection = Collection.objects.get(collection_name=kwargs.get('collection', ''))

	if request.user == collection.author:
		if request.method == 'GET':
			return render(request, 'collections/collection.html', {'collection': collection})

def collection_search_item(request, **kwargs):
	try:
		
		search_items = request.POST['q']

	except:
		return HttpResponseRedirect('collections/')

	if not search_items == '':
		results = SearchQuerySet().auto_query(search_items)

		return render(request, 'search/search.html', {'items': results})
	else:
		return render(request, 'search/search.html')

#def add_item(request, **kwargs):


