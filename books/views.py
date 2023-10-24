from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from .serializers import BookSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'index.html')

# get all books
def get_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return JsonResponse(list(books.values()), safe=False)
    return JsonResponse({'message': 'Invalid request'}, status=400)

# get book by id    
def get_books_by_id(request, pk):
    try:
        books = Book.objects.get(pk=pk)
        data = {
            'id': books.id,
            'title': books.title,
            'author': books.author,
            'desc': books.desc,
        }
        return JsonResponse(data)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'Book does not exist'}, status=404)

# create book with serializers class
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# update book by id
@csrf_exempt
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        if request.method == 'PUT':
            data = json.loads(request.body)
            book.title = data['title']
            book.author = data['author']
            book.desc = data['desc']
            book.save()
            return JsonResponse({'message': 'Book updated successfully'})
        return JsonResponse({'message': 'Invalid request'}, status=400)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'Book does not exist'}, status=404)

# delete book by id
@csrf_exempt
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'})
    except Book.DoesNotExist:
        return JsonResponse({'message': 'Book does not exist'}, status=404)
    