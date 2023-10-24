from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.get_books, name='get_books'),
    path('books/<int:pk>/', views.get_books_by_id, name='get_books_by_id'),
    path('books/create', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/delete', views.delete_book, name='delete_book'),
    path('books/<int:pk>/update', views.update_book, name='update_book'),
]
