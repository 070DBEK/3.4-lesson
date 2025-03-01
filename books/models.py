from django.db import models
from authors.models import Author


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=100)
    published_date = models.DateField()
    description = models.TextField()
    page_count = models.IntegerField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Copy(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    inventory_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)  # choices qo‘shildi
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "copies"

    def __str__(self):
        return f"{self.book.title} - {self.inventory_number} ({self.get_condition_display()})"

