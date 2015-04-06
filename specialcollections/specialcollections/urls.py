from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from specialcollections.views import home_view
#from collection_item.views import get_item, search_item
from collection_item.forms import ItemForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='home'),    
    url(r'^collections/', include('collection.urls', namespace="collections")),
    url(r'^collectiondb/', include('collection_item.urls', namespace="items")),
 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
