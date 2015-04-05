from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from specialcollections.views import home_view
from collection_item.views import get_item, search_item
from collection_item.forms import ItemForm, AdvancedItemSearchForm
from haystack.views import SearchView
from haystack.forms import SearchForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='home'),    
    url(r'^collections/', include('collection.urls', namespace="collections")),
    url(r'^collectiondb/', include('collection_item.urls', namespace="items")),
    url(r'^item/', get_item, name='item'),
   	#(r'^search/', SearchView(template='search.html', searchqueryset=sqs, form_class=AdvancedItemSearchForm)),
	#(r'^search/', include('haystack.urls')),
	url(r'^search/', search_item, name='search'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
