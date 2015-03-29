from django.conf.urls import patterns, include, url
from django.contrib import admin
from specialcollections.views import home_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='home'),    
    url(r'^collections/', include('collection.urls', namespace="collections")),
    url(r'^collectiondb/', include('collection_item.urls', namespace="items")),
)
