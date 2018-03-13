from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	UserListAPIView,
	UserGet,
	Logout
    )

urlpatterns = [
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^$', UserListAPIView.as_view(), name='list'),
	url(r'^by/(?P<email>[\w.@+-]+)/$', UserGet.as_view(), name='user_get'),
	url(r'^logout/', Logout.as_view()),
	
]