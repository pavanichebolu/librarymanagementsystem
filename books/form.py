# from django import forms
# from .models import Book

# class book_form(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = [
#             'title','isbn',' copies_available'
#         ]
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title name'}),
#             'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter isbn Number'}),
#             'copies_available': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter  copies available'}),
            
#         }
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'copies_available']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN'}),
            'copies_available': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of copies available'}),
        }