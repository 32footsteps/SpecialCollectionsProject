from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from specialcollections.views import home_view
from collection_item.views import get_item

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='home'),    
    url(r'^collections/', include('collection.urls', namespace="collections")),
    url(r'^collectiondb/', include('collection_item.urls', namespace="items")),
    url(r'^item/', get_item, name='item'),
    url(r'^search/', include('haystack.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
