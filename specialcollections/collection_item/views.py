from django.core.urlresolvers import reverse
from collection_item.models import Item
from collection_item.forms import ItemForm
from django.shortcuts import render
from django.contrib import messages
from django.template import Context, Template
from django.http import HttpResponseRedirect
from haystack.query import SearchQuerySet
from haystack.forms import SearchForm
from collection_item.forms import ItemForm

def index_view(request):
	return render(request, 'items/index.html')#, {'collections': collections})

def create_item(request):

	if request.method == 'POST':
		form = ItemForm(request.POST, request.FILES)
		user = request.user

		if form.is_valid():
			item = form.save(commit=False)
			item.creator = user			
			item.save()
			form.save()
			print("item save item image" + str(item.item_image))
			messages.add_message(request, messages.INFO, 'Item Created')
			return HttpResponseRedirect(reverse('items:index'))

	else:
		form = ItemForm()
	
	return render(request, 'items/createitem.html', {'form': form})

def get_item(request, **kwargs):
	item = Item.objects.get(title=kwargs.get('item', ''))
	print("title " + str(item.title))

	if request.method == 'GET':
		return render(request, 'items/item.html', {'item': item})	

def search_item(request):
	try:
		search_items = request.GET['q']

	except:
		return HttpResponseRedirect('collectiondb/')

	results = SearchQuerySet().auto_query(search_items)

	return render(request, 'items/index.html', {'items': results})	
