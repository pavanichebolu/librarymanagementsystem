from django.db import models

# Create your models here.
from authors.models import Author
from publishers.models import Publisher

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    
    isbn = models.CharField(max_length=13, unique=True)
    copies_available = models.PositiveIntegerField(default=1)


    def _str_(self):
        return self.title