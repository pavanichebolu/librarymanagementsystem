

# Create your views here.
# from django.shortcuts import render
# from . form import book_form
# def book_create(request):
#     form = book_form()
#     return render(request, 'books/book_form.html', {'form': form})
   
from django.shortcuts import render, redirect
from .form import BookForm

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')  # Redirect to a view that lists books or any other page
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})