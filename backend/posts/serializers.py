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
            "slug",
        ]

    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj).count()
        return qs

    def get_url(self, obj):
        return obj.get_api_url()


class PostDetailSerializer(serializers.ModelSerializer):
    # slug = serializers.SerializerMethodField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj)
        try:
            serializer = CommentSerializer(qs, many=True)
        except Exception as e:
            print(e)
        return serializer.data

    class Meta:
        model = Post
        fields = [
            "id",
            "slug",
            "title",
            "description",
            "body",
            "author",
            "created_at",
            "updated_at",
            "comments",
        ]
        extra_kwargs = {
            "slug": {"read_only": True},
        }

        # def get_slug(self, obj):
        #     return obj.slug


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "parent",
            "author",
            "body",
            "created_at",
            "updated_at",
        ]


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "body",
        ]