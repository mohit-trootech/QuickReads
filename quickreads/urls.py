from django.contrib import admin
from django.urls import path, include
from quickreads.views import HomeView, CreateBookView, BooksView
from quickreads.utils.constants import Urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", HomeView.as_view(), name=Urls.HOME_REVERSE.value),
    path("books/", BooksView.as_view(), name=Urls.BOOKS_REVERSE.value),
    path("create/", CreateBookView.as_view(), name=Urls.CREATE_BOOK_REVERSE.value),
]
