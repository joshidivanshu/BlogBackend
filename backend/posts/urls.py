from django.urls import path
from .views import (CreatePostAPIView,
                    ListPostAPIView,
                    DetailPostAPIView,
                    CreateCommentAPIView,
                    ListCommentAPIView,
                    )

app_name = "posts"

urlpatterns = [
    path("create/", CreatePostAPIView.as_view(), name="create-post"),
    path("", ListPostAPIView.as_view(), name='list-posts'),
    path("<str:slug>/", DetailPostAPIView.as_view(), name="post_detail"),
    path("<str:slug>/comment/", ListCommentAPIView.as_view(), name="list_comment"),
    path(
            "<str:slug>/comment/create/",
            CreateCommentAPIView.as_view(),
            name="create_comment",
        ),
]
