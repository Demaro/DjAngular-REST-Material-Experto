from django.conf.urls import url

from .views import (
	StatusDetailAPIView,
	StatusListAPIView,
	StatusUpdateAPIView, 
	StatusDeleteAPIView,
	StatusCreateAPIView,
	)

urlpatterns = [
    url(r'^$', StatusListAPIView.as_view(), name='list'),
    url(r'^create/$', StatusCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>[\w-]+)/$', StatusDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', StatusUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', StatusDeleteAPIView.as_view(), name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
