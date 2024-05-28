from django.urls import path 

from .  import views



urlpatterns = [
     path('book/<int:copies_available>/', views.book_details, name='book_details'),

     
]
