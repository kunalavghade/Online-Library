from django.contrib import admin
from django.urls import path,include
from library import views

urlpatterns = [
    path('',views.index,name="index page"),
    path('login',views.login,name="login")
]