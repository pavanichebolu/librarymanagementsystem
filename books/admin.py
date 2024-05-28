from django.contrib import admin
from .models import Book
from authors.models import Author
from loans.models import Loan

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Loan)

# Register your models here.
