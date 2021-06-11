from django.urls import path
from .views import CreatePostAPIView, ListPostAPIView

app_name = "posts"

urlpatterns = [
    path("create/", CreatePostAPIView.as_view(), name="create-post"),
    path("", ListPostAPIView.as_view(), name='list-posts'),
]