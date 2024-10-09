from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, BookRecords, Profile, UserType


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Profile(
            user=user,
            user_type=UserType.LIBRARIAN,
            created_by=user,
        ).save()

        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "is_available",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = user
        return super().create(validated_data)


class ListOfBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "is_available",
        ]


class ListOfMembersSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "is_active",
        ]

    def get_username(self, obj):
        return obj.user.username

    def get_is_active(self, obj):
        return obj.user.is_active


class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Profile(
            user=user,
            user_type=UserType.MEMBER,
            created_by=user,
        ).save()

        return user


class BookRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRecords
        fields = [
            "member",
            "book",
        ]
