from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'nationality')
    search_fields = ('first_name', 'last_name', 'nationality')
    list_filter = ('nationality', 'birth_date')
    ordering = ('last_name',)

