from django.contrib.auth import authenticate, login
from rest_framework import serializers, status
from rest_framework.authentication import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import Book


def check_user_data(serializer, request):
    if not serializer.is_valid():
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    username = serializer.validated_data["username"]
    password = serializer.validated_data["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Login successful!",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            },
            status=status.HTTP_200_OK,
        )
    return Response(
        {
            "error": "Invalid credentials",
        },
        status=status.HTTP_400_BAD_REQUEST,
    )


def member_book_borrowed(serializer):
    book = serializer.validated_data["book"]
    if not book.is_available:
        raise serializers.ValidationError("This book is currently not available.")

    book_record = serializer.save()
    book.is_available = False
    book.save()
    return book_record
