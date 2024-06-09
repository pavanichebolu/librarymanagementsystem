from django.contrib import admin 
from django.urls import path , include, re_path
from django.conf.urls.static import static 
from django.conf import  settings 
from . import views

from .views import index,books,authors,loans,members,publishers
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
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

path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),