from rest_framework import generics, status, pagination
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models


class BookListCreateView(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    pagination_class = pagination.PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fir', 'price']