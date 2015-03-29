from django.conf.urls import patterns, include, url
from django.contrib import admin
from collection_item import Item


urlpatterns = patterns('',
		url(r'$', index_view, name='index'),
)