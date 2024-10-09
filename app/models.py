from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserType(models.IntegerChoices):
    LIBRARIAN = 1, "Librarian"
    MEMBER = 2, "Member"


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(choices=UserType.choices)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="added_by"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "profiles"


class Book(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "books"


class BookRecords(BaseModel):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.user.username} borrowed {self.book.title}"
    
    class Meta:
        db_table = "book_records"
