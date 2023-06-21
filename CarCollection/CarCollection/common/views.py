from django.shortcuts import render


def index(request):
    return render(
        request,
        'common/index.html',
    )


def catalogue(request):
    return render(
        request,
        'common/catalogue.html',
    )
