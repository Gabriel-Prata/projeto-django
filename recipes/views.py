import datetime
from django.shortcuts import render
from utility.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
        'name': 'Gabriel Prata',
        'data': datetime.datetime.now()
        })


def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
