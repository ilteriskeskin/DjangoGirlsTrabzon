from django.contrib import admin
from django.urls import path,include
from . import views

app_name ="user"

urlpatterns =[
    path('registerUser/',views.registerUser,name="registerUser"),
    path('loginUser/',views.loginUser,name="loginUser"),
    path('logoutUser/',views.logoutUser,name="logoutUser"),
]