from django.db import models

class Book(models.Model):
    title = models.TextField()
    year = models.CharField(max_length=10)
    isbn = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
