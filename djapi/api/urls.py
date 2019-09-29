from django.urls import path
from api.apiViews import BooksList, BooksDetalle, BookSave

urlpatterns = [
    path('v1/books/', BooksList.as_view(), name='books_list'),
    path('v1/books/<int:pk>', BooksDetalle.as_view(), name='book_detalle'),
    path('v1/books/add/', BookSave.as_view(), name='book_add')
]