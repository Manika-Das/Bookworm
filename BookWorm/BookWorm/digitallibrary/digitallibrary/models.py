from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    thumbnail_url = models.URLField()
    ratings = models.FloatField()
    pdf_link = models.URLField()
    language = models.CharField(max_length=50)
    isbn_number = models.CharField(max_length=20, unique=True)
    publishing_date = models.DateField()
    book_pages = models.IntegerField()

    def __str__(self):
        return f"{self.book_name} by {self.author_name}"