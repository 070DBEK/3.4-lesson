from rest_framework import serializers
from .models import Genre, Book, BookCopy, BookLending
from authors.models import Author


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'genre', 'isbn', 'published_date',
            'description', 'page_count', 'language'
        ]


class BookCopySerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BookCopy
        fields = [
            'id', 'book', 'inventory_number', 'condition',
            'is_available', 'added_date'
        ]


class BookLendingSerializer(serializers.ModelSerializer):
    book_copy = serializers.PrimaryKeyRelatedField(queryset=BookCopy.objects.all())

    class Meta:
        model = BookLending
        fields = [
            'id', 'book_copy', 'borrowed_name', 'borrowed_email',
            'borrowed_date', 'due_date', 'returned_date', 'status'
        ]
