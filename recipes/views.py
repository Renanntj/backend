from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
# HTTP Requests --> Response
def home(requests): 
    return render(requests, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })
def recipe(requests, id): 
    return render(requests, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })





