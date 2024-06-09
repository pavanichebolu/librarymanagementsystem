
from django.shortcuts import render, redirect
from .form import BookForm

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')  
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})