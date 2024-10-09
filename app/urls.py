from django.urls import path

from .views import (
    BookCreateAPIView,
    BookDestroyAPIView,
    BookUpdateAPIView,
    DeleteMyAccountAPIView,
    ListOfBooksAPIView,
    ListOfMembersAPIView,
    LoginAPIView,
    MemberBookAPIView,
    MemberCreateAPIView,
    MemberDestroyAPIView,
    MemberHistoryListAPIView,
    MemberUpdateAPIView,
    SignupAPIView,
)

urlpatterns = [
    # SIGNUP
    path(
        "signup",
        view=SignupAPIView.as_view(),
        name="user_signup",
    ),
    # LOGIN
    path(
        "login",
        view=LoginAPIView.as_view(),
        name="user_login",
    ),
    # LIBRARIAN
    path(
        "books",
        view=BookCreateAPIView.as_view(),
        name="add_books",
    ),
    path(
        "list-of-books",
        view=ListOfBooksAPIView.as_view(),
        name="view_books",
    ),
    path(
        "list-of-members",
        view=ListOfMembersAPIView.as_view(),
        name="view_members",
    ),
    path(
        "books/<int:id>",
        view=BookDestroyAPIView.as_view(),
        name="delete_book",
    ),
    path(
        "books/update/<int:id>",
        view=BookUpdateAPIView.as_view(),
        name="update_book",
    ),
    path(
        "members",
        view=MemberCreateAPIView.as_view(),
        name="add_member",
    ),
    path(
        "members/borrowed-book",
        view=MemberBookAPIView.as_view(),
        name="member-borrowed-book",
    ),
    path(
        "members/update/<int:id>",
        view=MemberUpdateAPIView.as_view(),
        name="update_member",
    ),
    path(
        "members/history",
        view=MemberHistoryListAPIView.as_view(),
        name="members_history",
    ),
    path(
        "members/<int:member_id>",
        view=MemberDestroyAPIView.as_view(),
        name="delete_member",
    ),
    # MEMBERS
    path(
        "delete_account",
        view=DeleteMyAccountAPIView.as_view(),
        name="delete_account",
    ),
]
