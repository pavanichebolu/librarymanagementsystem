from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)  # Hypothetical password hashing function

    if user is not None:
      auth.login(request, user)
      return redirect("/addbook")
    else:
      messages.info(request, 'Invalid credentials')
      return redirect('login')

  else:
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        book=request.POST['book']
        member=request.POST['member']
        loan_date=request.POST['loan_date']
        return_date=request.POST['return_date']
        due_date=request.POST['due_date']
    
        if loan_date== member:
            if User.objects.filter(loan_date).exists(): 
                messages.info(request,'book Already Taken')
                return redirect('register')
            elif User.objects.filter(member=member).exists(): 
                messages.info(request,'members Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(member=member,loan_date=loan_date,book=book,return_date=return_date,duw_date=due_date)
                user.save()
                messages.info(request,'Sucessfully User Register')
                return redirect('login')
        else:
              messages.info(request,'loan_date and member is not match')
              return redirect('/register')
        
    else:
        return render(request, 'register.html')

def logout(request):
  auth.logout(request)
  return redirect('/')
def loans(request):
   return render(request,loans.html)


def loan_details(request):
    # Your logic here
    return render(request, 'loan_details.html')