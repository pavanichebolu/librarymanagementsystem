from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book



def index(request):
    return render(request,"index.html")

def books(request):
    books = Book.objects.all() 
    return render(request,"books.html", {'books' : books})

def authors(request):
    authors = Book.objects.all() 
    return render(request,"authors.html", {'authors' : authors})

def publishers(request):
    return render(request,"publishers.html")


def loans(request):
    return render(request,"loans.html")

def addbook(request):
    if request.method=='POST':
       book_name=request.POST['book_name'] 
       isbn=request.POST['isbn']
       author_name=request.POST['author_name']
       book_pages=request.POST['book_pages']
        
    b=Book(book_name=book_name,isbn=isbn,author_name=author_name,book_pages=book_pages)
    b.save()
    return render(request,"addbook.html")

def members(request):
    return render(request,"members.html")