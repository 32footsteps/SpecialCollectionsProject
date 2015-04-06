from django.conf.urls import patterns, include, url
from django.contrib import admin
from collection.views import index_view, create_collection, get_collection


urlpatterns = patterns('',
		url(r'^$', index_view, name='index'),
		url(r'^createcollection/', create_collection, name='createcollection'),
		url(r'^(?P<collection>(?!\s*$).+)', get_collection, name='getcollection'),
)