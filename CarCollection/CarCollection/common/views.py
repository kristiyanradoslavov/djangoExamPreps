from django.shortcuts import render, redirect

from CarCollection.util_functions.get_cars import get_cars
from CarCollection.util_functions.get_profile import get_profile


def index(request):

    context = {
        'profile': get_profile()
    }

    return render(
        request,
        'common/index.html',
        context
    )


def catalogue(request):
    if not get_profile():
        return redirect('index')

    context = {
        'cars': get_cars(),
        'profile': get_profile(),
    }
    return render(
        request,
        'common/catalogue.html',
        context
    )
