from django.urls import path, include
from OnlineLibrary.books_and_home.views import book_add, book_edit, book_details, home_page, book_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path('add/', book_add, name='add book'),
    path('edit/<int:book_id>/', book_edit, name='edit book'),
    path('details/<int:book_id>/', book_details, name='book details'),
    path('delete/<int:book_id>/', book_delete, name='book delete'),
]
