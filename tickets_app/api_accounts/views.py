from django.db.models import Q
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView, 
	UpdateAPIView, 
	DestroyAPIView, 
	CreateAPIView
	)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin


from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)


from rest_framework import generics

User = get_user_model()


from .serializers import ( 
	UserCreateSerializer,
	UserLoginSerializer,
	UserDetailSerializer
	)

from braces.views import CsrfExemptMixin


class UserGet(generics.ListAPIView):
	serializer_class = UserDetailSerializer 


	def get_queryset(self):
		email = self.kwargs['email']

		return User.objects.filter(email=email)


class UserCreateAPIView(CsrfExemptMixin, CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()
	authentication_classes = []


class UserLoginAPIView(CsrfExemptMixin, APIView):
	authentication_classes = []
	#permissions_classes = [AllowAny]
	serializer_class = UserLoginSerializer
	

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserListAPIView(CsrfExemptMixin, ListAPIView):
	queryset                = User.objects.all().order_by('-id')
	serializer_class        = UserDetailSerializer
	authentication_classes = []


from rest_framework import status


class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
