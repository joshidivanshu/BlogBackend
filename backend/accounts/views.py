from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import  Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView
)
from .serializers import UserSerializer, UserUpdateSerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    # these results are cached for all the subsequent requests
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
        get:
            Returns the detail of a user instance
            parameters: [id]

        put:
            Update the detail of a user instance
            parameters: [id, username, email, password]

        delete:
            Delete a user instance

            parameters: [id]
    """
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Returns an object instance that should be used for detail views. Defaults to using the
    # lookup_field parameter to filter the base queryset
    lookup_field = 'id'


class UserUpdateView(UpdateAPIView):

    def get_queryset(self):
        query_set = User.objects.all()
        return query_set

    serializer_class = UserUpdateSerializer
    lookup_field = 'id'
    # def perform_update(self, serializer):
    #     instance = serializer.save()



