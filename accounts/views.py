from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages,auth
# Create your views here.
def register(request):
    return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('books')  # Adjust this to redirect to the appropriate dashboard based on user type
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')