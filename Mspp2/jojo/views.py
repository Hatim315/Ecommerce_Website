"""jojo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
""" an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.jango.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.home,name="Home"),
    path('about',views.about,name="About"),
    path('services',views.services,name="Services"),
    path('products',views.products,name="Products"),
    path('login',views.Login,name="Login"),
    path('logout',views.Logout,name="Logout"),
    path('createnewaccount',views.cna,name="Creatur views here.

"""
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from jojo.models import Contact
from django.contrib import  messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def about(request):
    if request.method=="POST":
        naam=request.POST.get('name')
        phno=request.POST.get('phone')
        emale=request.POST.get('email')
        des=request.POST.get('desc')
        contact=Contact(name=naam,email=emale,phone=phno,desc=des,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent!')
    return render(request,'about.html')
def products(request):
    
    return render(request,'product.html')

def Login(request):
    if request.method=="POST":
        usename=request.POST.get('username')
        pasword=request.POST.get('password')
        
        
        user=authenticate(username=usename,password=pasword)
       
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            
            return HttpResponse("No user with this name found. Please Sign Up.")
    return render(request,"login.html")
    
def Logout(request):
    logout(request)
    return redirect(("/login"))
def home(request):
    username=request.user
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html",{'username':username})
def cna(request):
    if request.method=="POST":
        usrn=request.POST.get("username")
        passwd=request.POST.get("password")
        cpasswd=request.POST.get("cpassword")
        emal=request.POST.get("email")
        try:
           if passwd==cpasswd:
              user=User.objects.create_user(usrn,emal,passwd)
              user.save()
              return redirect("/login")
           else:
               return redirect("/createnewaccount")
               messages.success(request,"Passwords did not match")

        except:
            messages.success(request,"Username not available")
    return render(request,'create.html')
    
    # return HttpResponse("This is the homepage")
