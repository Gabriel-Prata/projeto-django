import datetime

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Gabriel',
        'data': datetime.datetime.now()
        })


def contato(request):
    return HttpResponse('Texto')


def sobre(request):
    return HttpResponse('SOBRE 1')

