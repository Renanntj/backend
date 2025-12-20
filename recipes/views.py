from django.shortcuts import render
from django.http import HttpResponse

# HTTP Requests --> Response
def home(requests): 
    return render(requests, 'recipes/home.html', context={
        'nome': 'Renan',
    })

def contato(requests):
    return render(requests, 'recipes/contato.html')

def sobre(requests):
    return HttpResponse("Sobre")




