from django.contrib import admin
from django.urls import path
from appfile import views

urlpatterns = [
     path("",views.index,name='index'),
]