from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

# HTTP Requests --> Response
def home(requests): 
    return HttpResponse("Hello World, Django!")
def contato(requests):
    return HttpResponse("Contato")
def sobre(requests):
    return HttpResponse("Sobre")



urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]

