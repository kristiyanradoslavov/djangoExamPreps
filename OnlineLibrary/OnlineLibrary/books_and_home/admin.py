from django.contrib import admin

from OnlineLibrary.books_and_home.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
