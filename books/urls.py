from django.urls import path
from .views import *


urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),

    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('books/<int:book_id>/copies/', BookCopiesListView.as_view(), name='book-copies'),

    path('copies/', BookCopyListCreateView.as_view(), name='book-copy-list-create'),
    path('copies/<int:pk>/', BookCopyRetrieveUpdateDestroyView.as_view(), name='book-copy-detail'),

    path('lendings/', BookLendingListCreateView.as_view(), name='book-lending-list-create'),
    path('lendings/<int:pk>/', BookLendingRetrieveUpdateDestroyView.as_view(), name='book-lending-detail'),
]
