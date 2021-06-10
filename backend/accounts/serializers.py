from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(allow_blank=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("length of username should be greater than 5")
        return value

    def validate(self, data):
        if len(data['password']) < 8 or len(data['password']) > 32:
            raise serializers.ValidationError("Password length should be greater than 8 & less than 32")
        if len(data['email']) > 50:
            raise serializers.ValidationError("Length of email shoul be less than 50")
        return data


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(min_length=8, max_length=32, write_only=True)
    email = serializers.EmailField(max_length=50, allow_blank=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


# class UserDeleteSerializer(serializers.ModelSerializer):
#     id = serializers.PrimaryKeyRelatedField(read_only=True)
#     password = serializers.CharField(min_length=8, max_length=32, write_only=True)
#     email = serializers.EmailField(max_length=50, allow_blank=False)
#
#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "password"]



