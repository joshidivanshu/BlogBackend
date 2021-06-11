import os
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "body",
        ]

    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Max title length is 100")
        return value

    def validate_description(self, value):
        if len(value) > 200:
            return serializers.ValidationError(
                "Max description length is 200 characters"
            )
        return value

    # def clean_image(self, value):
    #     initial_path = value.path
    #     new_path = settings.MEDIA_ROOT + value.name
    #     os.rename(initial_path, new_path)
    #     return value

    def create(self, validated_data):
        post = Post()
        post.title = validated_data["title"]
        post.body = validated_data["body"]
        print(validated_data["description"])
        post.description = validated_data["description"]
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            post.author = User.objects.filter(id=request.user.id).first()
        # post.image = validated_data["image"]
        post.save()
        return validated_data


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "url",
            "title",
            "author",
            "description",
            "comments",
        ]

    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj).count()
        return qs

    def get_url(self, obj):
        return obj.get_api_url()

