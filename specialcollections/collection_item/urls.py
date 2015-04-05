from django.conf.urls import patterns, include, url
from django.contrib import admin
from collection_item.views import index_view, create_item, search_item


urlpatterns = patterns('',
		url(r'^$', index_view, name='index'),
		url(r'^createitem/', create_item, name='createitem'),
		url(r'^searchitem/', search_item, name='searchitem'),
)