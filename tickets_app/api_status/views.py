from django.contrib.auth.models import User

from rest_framework import generics


from tickets_app.models import Status

from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView, 
	UpdateAPIView, 
	DestroyAPIView, 
	CreateAPIView
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly


from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)


from django.db.models import Q

from .serializers import ( 
	StatusCreateSerializer, 
	StatusListSerializer, 
	StatusDetailSerializer
	)

from braces.views import CsrfExemptMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StatusListAPIView(ListAPIView):
	queryset                = Status.objects.all().order_by('-id')
	serializer_class        = StatusListSerializer
	permission_classes = [AllowAny]





class StatusCreateAPIView(CsrfExemptMixin, CreateAPIView):
	authentication_classes = []
	queryset = Status.objects.all()
	serializer_class = StatusCreateSerializer
	#permission_classes = [IsAuthenticated]



class StatusDetailAPIView(RetrieveAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusDetailSerializer
	lookup_field = 'id'
	permission_classes = [AllowAny]


class StatusUpdateAPIView(CsrfExemptMixin, RetrieveUpdateAPIView):
	authentication_classes = []
	queryset = Status.objects.all()
	serializer_class = StatusCreateSerializer
	lookup_field = 'id'



class StatusDeleteAPIView(CsrfExemptMixin, DestroyAPIView):
	authentication_classes = []
	queryset = Status.objects.all()
	serializer_class = StatusDetailSerializer
	lookup_field = 'id'



