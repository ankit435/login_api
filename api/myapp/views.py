from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.http import HttpResponse 
from django.shortcuts import render ,redirect



def login(request):
    return render(request ,'auth/login.html')

    
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email_id']
        password =request.POST['password']
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()
        print("user creayed")
        return redirect('login')
    else:
          return render(request ,'auth/up.html')
def sucess(request):
    pass
# Create your views here.
