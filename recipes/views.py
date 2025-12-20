from django.shortcuts import render
from django.http import HttpResponse

# HTTP Requests --> Response
def home(requests): 
    return render(requests, 'recipes/home.html', context={
        'nome': 'Renan',
    })





