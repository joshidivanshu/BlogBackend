from django.urls import path
from .views import (UserCreateAPIView,
                    UserListAPIView,
                    UserDetailAPIView,
                    UserUpdateView
                    )

app_name = "accounts"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    # path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
    path("<int:id>/", UserUpdateView.as_view(), name="user_detail"),
]