from django.contrib import admin 
from django.urls import path , include, re_path
from django.conf.urls.static import static 
from django.conf import  settings 


from .views import index,books,authors,loans,members,addbook,publishers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('books/', books, name='books'),
    
    path('authors/', authors, name='authors'),
    path('loans/', include('loans.urls')),
    path('members/', members, name='members'),
    path('addbook/', addbook, name='addbook'),
    path('publishers/', publishers, name='publishers'),
    
    path('books/', include('books.urls')),

   
    # re_path(r'^.*$', index, name='index')
   
]
