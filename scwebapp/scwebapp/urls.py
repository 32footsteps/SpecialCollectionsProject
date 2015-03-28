from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from scwebapp.views import IndexView
from collection.views import SCUserCollectionViewSet, CollectionViewSet
from collection_user.views import SCUserViewSet, LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'scusers', SCUserViewSet)
router.register(r'collections', CollectionViewSet)

scuser_router = routers.NestedSimpleRouter(
	router, r'scusers', lookup='scuser'
)

scuser_router.register(r'collections', SCUserCollectionViewSet)

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(scuser_router.urls)),    
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^.*$', IndexView.as_view(), name="index"),


)
