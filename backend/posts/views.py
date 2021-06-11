from django.shortcuts import render
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Post, Comment
from .serializers import (
    PostCreateUpdateSerializer,
    PostListSerializer
)


class CreatePostAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Post created successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPostAPIView(ListAPIView):
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostListSerializer


# class DetailPostAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     lookup_field = "slug"
#     serializer_class = PostDetailSerializer
#     permission_classes = [AllowAny]

