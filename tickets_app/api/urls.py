from django.conf.urls import url

from .views import (
	TicketDetailAPIView,
	TicketListAPIView,
	TicketUpdateAPIView, 
	TicketDeleteAPIView,
	TicketCreateAPIView,
	)

urlpatterns = [
    url(r'^$', TicketListAPIView.as_view(), name='list'),
    url(r'^create/$', TicketCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>[\w-]+)/$', TicketDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', TicketUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', TicketDeleteAPIView.as_view(), name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
