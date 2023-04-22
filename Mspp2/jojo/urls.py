#tion views
from django.contrib import admin
from django.urls import path,include
from jojo import views
from shop.views import showproducts
urlpatterns = [
    path('',views.home,name="Home" ),
    path('about',views.about,name="About"),
    
    path('products',showproducts,name="Products"),
    path('login',views.Login,name="Login"),
    path('logout',views.Logout,name="Logout"),
    path('createnewaccount',views.cna,name="CreateNewAccount")
    
]


