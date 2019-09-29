# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Books
from .serializers import BookSerializer

class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BooksDetalle(generics.RetrieveDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookSave(generics.CreateAPIView):
    serializer_class = BookSerializer