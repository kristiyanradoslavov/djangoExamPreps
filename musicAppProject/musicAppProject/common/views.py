# common views

from django.shortcuts import render


def home_page(request):
    return render(request, 'common/home-no-profile.html')
