from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Registerform

# Create your views here.
def home(request):
    if(request.method=='POST'):
        username=request.POST['un']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if(user is not None):
            login(request,user)
            messages.success(request,'you are successfully logged in !')
            return redirect('home')
        else:
            messages.error(request,'credentials did not match try again!')
            return redirect('home')



    return render(request,'home.html')


def logout_user(request):
    logout(request)
    messages.success(request,'you are successfully loggedout !')
    return redirect('home')

def register(request):
    form=Registerform()
    if(request.method=='POST'):
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your account has been created please login!')
            return redirect('home')
        else:
            messages.success(request,' Provide correct details please try again!')
            return redirect('register')
        
    else:
        context={
            'form':form
        }
        return render(request,'register.html',context)
    
    