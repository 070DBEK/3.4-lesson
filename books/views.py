from rest_framework import generics, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers
from authors.views import CustomPagination


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer

    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genre', 'language', 'published_date']
    search_fields = ['title', 'isbn']


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookCopyListCreateView(generics.ListCreateAPIView):
    queryset = models.BookCopy.objects.all()
    serializer_class = serializers.BookCopySerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['book', 'condition', 'is_available']
    search_fields = ['inventory_number']


class BookCopyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BookCopy.objects.all()
    serializer_class = serializers.BookCopySerializer


class BookLendingListCreateView(generics.ListCreateAPIView):
    queryset = models.BookLending.objects.all()
    serializer_class = serializers.BookLendingSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'borrowed_name']
    search_fields = ['borrowed_email']


class BookLendingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BookLending.objects.all()
    serializer_class = serializers.BookLendingSerializer


class BookCopiesListView(generics.ListAPIView):
    serializer_class = serializers.BookCopySerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return models.BookCopy.objects.filter(book__id=book_id).order_by('added_date')

