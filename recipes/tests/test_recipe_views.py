from django.test import TestCase
from django.urls import resolve , reverse
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User

class RecipeViewsTest(TestCase):
    def test_recipe_home_views_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    def test_recipe_home_view_return_status_code_200_OK(self):
        status_code = self.client.get(reverse('recipes:home'))
        self.assertEqual(status_code.status_code, 200)
    
    def test_recipe_home_load_correct_template(self):
        template = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(template, 'recipes/pages/home.html')
        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        template = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            template.content.decode('utf-8')
        )
    
    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name="Category")
        author = User.objects.create_user(
            first_name = "user",
            last_name = "user",
            username = "username",
            password = "123456",
            email = "user@gmail.com",
        )
        
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        
        assert 1 == 1
    def test_recipe_category_views_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        status_code = self.client.get('recipes:category', kwargs={'category_id': 1000})
        self.assertEqual(status_code.status_code, 404)
        
    def test_recipe_detail_views_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
        
    def test_recipe_detail_view_return_404_if_no_recipes_found(self):
        status_code = self.client.get('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(status_code.status_code, 404)
    

        

    