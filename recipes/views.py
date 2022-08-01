import datetime
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'GABRIEL',
        'data': datetime.datetime.now()
        })
