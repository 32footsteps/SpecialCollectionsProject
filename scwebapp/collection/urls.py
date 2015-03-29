from django.conf.urls import patterns, include, url
from django.contrib import admin
from collection.views import index_view


urlpatterns = patterns('',
		url(r'^$', index_view, name='index'),
)