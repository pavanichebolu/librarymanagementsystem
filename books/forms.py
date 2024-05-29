from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title','isbn',' copies_available'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title name'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter isbn Number'}),
            'copies_available': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter  copies available'}),
            
        }