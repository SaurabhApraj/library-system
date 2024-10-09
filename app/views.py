from django.contrib.auth.models import User
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
)

from .models import Book, Profile
from .serializers import (
    BookSerializer,
    ListOfBookSerializer,
    ListOfMembersSerializer,
    LoginSerializer,
    MemberSerializer,
    SignupSerializer,
)
from .services import check_user_data, member_book_borrowed


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return check_user_data(serializer, request)


class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer


class ListOfBooksAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ListOfBookSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user.id)


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    lookup_field = "id"
    serializer_class = BookSerializer


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = "id"


class ListOfMembersAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ListOfMembersSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)


class MemberCreateAPIView(CreateAPIView):
    serializer_class = MemberSerializer


class MemberUpdateAPIView(UpdateAPIView): ...


class MemberDestroyAPIView(DestroyAPIView):
    queryset = Profile.objects.all()
    lookup_field = "id"


class MemberHistoryListAPIView(ListAPIView): ...


class DeleteMyAccountAPIView(DestroyAPIView): ...


class MemberBookAPIView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return member_book_borrowed(serializer, request)
