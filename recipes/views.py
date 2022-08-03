import datetime
from django.http import Http404
from django.shortcuts import render
from .models import Recipe


name = 'Gabriel Prata'
date = datetime.datetime.now()


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'name': name,
        'data': date,
        })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by('id')

    if not recipes:
        raise Http404('NONECXISTE')

    category_name = recipes.first().category.name

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'category_name': category_name,
        'name': name,
        'data': date,
        })




def recipes(request, recipe_id):
    recipe = Recipe.objects.filter(
        id=recipe_id,
        is_published=True,
    ).first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'name': name,
        'data': date,
    })
