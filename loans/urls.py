from django.urls import path 

from .  import views



urlpatterns = [
      path('loan/<int:copies_available>/', views.loan_details, name='loan_details'),
     
     
]


