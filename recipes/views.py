from django.shortcuts import render, get_list_or_404
from .models import Recipe
from utils.recipes.factory import make_recipe
# HTTP Requests --> Response
def home(requests): 
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(requests, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    


def category(requests, category_id): 

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
        
    return render(requests, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
    })    

def recipe(requests, id): 
    return render(requests, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })





