

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from . models import Book

def books_list(request):
    books =Book.objects.all()
    return render(request, 'books.html', {'books': books})



def book_details(request, title):
    book = get_object_or_404(Book, title=title)
    return render(request, 'book_details.html', {'book': book})
    