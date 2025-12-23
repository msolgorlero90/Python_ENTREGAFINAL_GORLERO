from django.db import models
from ckeditor.fields import RichTextField

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title