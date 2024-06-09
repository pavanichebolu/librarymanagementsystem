from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from authors.models import Author
from publishers.models import Publisher
from loans.models import Loan
from members.models import Member
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request,"index.html")

@login_required
def books(request):
    book = Book.objects.all()
    return render(request, "books.html" ,{'book': book})

@login_required  
def authors(request):
    authors = Author.objects.all()
    return render(request, "authors.html" ,{'authors': authors})

@login_required
def publishers(request):
    pub = Publisher.objects.all()
    return render(request, "publishers.html" ,{'pub': pub})

@login_required
def loans(request):
    lo = Loan.objects.all()
    return render(request, "loans.html" ,{'lo': lo})


@login_required
def members(request):
    mem = Member.objects.all()
    return render(request, "members.html" ,{'mem': mem})

@login_required
def forms(request):
    return render(request, 'book_form.html')

@login_required
def register(request):
    return render(request, "register.html")

@login_required
def login(request):
    return render(request, "login.html")
