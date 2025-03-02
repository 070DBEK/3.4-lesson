from rest_framework import generics, pagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AuthorSerializer
from books.serializers import BookSerializer
from .models import Author
from books.models import Book


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['birth_date', 'nationality']


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorBooksListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Book.objects.filter(author__id=author_id)