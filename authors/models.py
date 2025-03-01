from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()
    nationality = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"