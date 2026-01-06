from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
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
        'title': f'{recipes[0].category.name} - Category | '
    })    

def recipe(requests, id):
    
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(requests, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })





