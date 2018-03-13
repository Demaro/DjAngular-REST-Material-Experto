from django.contrib.auth.models import User

from rest_framework import generics


from tickets_app.models import Ticket

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
from .pagination import TicketLimitOffsetPagination, TicketPageNumberPagination

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)


from django.db.models import Q

from .serializers import ( 
	TicketCreateSerializer, 
	TicketListSerializer, 
	TicketDetailSerializer
	)

from braces.views import CsrfExemptMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TicketListAPIView(ListAPIView):
	queryset                = Ticket.objects.all().order_by('-id')
	serializer_class        = TicketListSerializer
	permission_classes = [AllowAny]





class TicketCreateAPIView(CsrfExemptMixin, CreateAPIView):
	authentication_classes = []
	queryset = Ticket.objects.all()
	serializer_class = TicketCreateSerializer
	#permission_classes = [IsAuthenticated]



class TicketDetailAPIView(RetrieveAPIView):
	queryset = Ticket.objects.all()
	serializer_class = TicketDetailSerializer
	lookup_field = 'id'
	permission_classes = [AllowAny]


class TicketUpdateAPIView(CsrfExemptMixin, RetrieveUpdateAPIView):
	authentication_classes = []
	queryset = Ticket.objects.all()
	serializer_class = TicketCreateSerializer
	lookup_field = 'id'



class TicketDeleteAPIView(CsrfExemptMixin, DestroyAPIView):
	authentication_classes = []
	queryset = Ticket.objects.all()
	serializer_class = TicketDetailSerializer
	lookup_field = 'id'



