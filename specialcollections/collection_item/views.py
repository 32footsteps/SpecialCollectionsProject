from django.core.urlresolvers import reverse
from collection_item.models import Item
from collection_item.forms import ItemForm
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect


def index_view(request):
	#collections = Collection.objects.all()
	return render(request, 'items/index.html')#, {'collections': collections})

def create_item(request):

	if request.method == 'POST':
		form = ItemForm(request.POST, request.FILES)
		user = request.user
		print("item"+str(user.username))

		if form.is_valid():
			print("form valid")
			item = form.save(commit=False)
			item.creator = user.username
			item.save()
			form.save()
			print("item save item image" + str(item.item_image))
			messages.add_message(request, messages.INFO, 'Item Created')
			return HttpResponseRedirect(reverse('items:index'))

	else:

		print("form empty")
		form = ItemForm()
	print("form in valid")
	messages.error(request, "Error")
	return render(request, 'items/createitem.html', {'form': form})