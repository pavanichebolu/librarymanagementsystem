from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book



def index(request):
    return render(request,"index.html")

def books(request):
    book = Book.objects.all()
    return render(request, "books.html" ,{'book': book})
    
def authors(request):
    
    return render(request,"authors.html")

def publishers(request):
    return render(request,"publishers.html")


def loans(request):
    return render(request,"loans.html")



def members(request):
    return render(request,"members.html")