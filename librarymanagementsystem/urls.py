from django.contrib import admin 
from django.urls import path , include, re_path
from django.conf.urls.static import static 
from django.conf import  settings 
from . import views

from .views import index,books,authors,loans,members,publishers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('books/', books, name='books'),
    
    path('authors/', authors, name='authors'),
    path('loans/', loans , name='loans'),
    path('members/', members, name='members'),
    
    path('publishers/', publishers, name='publishers'),

    path('accounts/', include('accounts.urls')),
    path('forms/', views.forms, name='forms'),
    # re_path(r'^.*$', index, name='index')
   
    path('books/', include('books.urls')),
]
