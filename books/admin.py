from django.contrib import admin
from .models import Genre, Book, BookCopy, BookLending


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'published_date', 'language')
    search_fields = ('title', 'isbn')
    list_filter = ('genre', 'language', 'published_date')
    ordering = ('title',)


@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date')
    search_fields = ('inventory_number',)
    list_filter = ('condition', 'is_available')


@admin.register(BookLending)
class BookLendingAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_copy', 'borrowed_name', 'status', 'borrowed_date', 'due_date', 'returned_date')
    search_fields = ('borrowed_name', 'borrowed_email')
    list_filter = ('status', 'borrowed_date', 'due_date', 'returned_date')
