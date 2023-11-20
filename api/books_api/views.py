from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books_api.models import Book
from books_api.serializer import BookSerializer

# Create your views here.

@api_view(['GET'])
def book_list(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)
