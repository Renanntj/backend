from django.shortcuts import render
from django.http import HttpResponse

# HTTP Requests --> Response
def home(requests): 
    return render(requests, 'recipes/home.html')

def contato(requests):
    return HttpResponse("Contato")

def sobre(requests):
    return HttpResponse("Sobre")




