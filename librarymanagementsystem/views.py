from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from authors.models import Author
from publishers.models import Publisher
from loans.models import Loan
from members.models import Member


def index(request):
    return render(request,"index.html")

def books(request):
    book = Book.objects.all()
    return render(request, "books.html" ,{'book': book})
    
def authors(request):
    authors = Author.objects.all()
    return render(request, "authors.html" ,{'authors': authors})

def publishers(request):
    pub = Publisher.objects.all()
    return render(request, "publishers.html" ,{'pub': pub})


def loans(request):
    lo = Loan.objects.all()
    return render(request, "loans.html" ,{'lo': lo})



def members(request):
    mem = Member.objects.all()
    return render(request, "members.html" ,{'mem': mem})

def forms(request):
    # Your view logic here
    return render(request, 'book_form.html')
