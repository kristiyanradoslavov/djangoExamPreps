from django.shortcuts import render, redirect

from FinalExam.util_functions.get_fruits import get_all_fruits
from FinalExam.util_functions.get_profile import get_profile


def index(request):
    context = {
        'profile': get_profile()
    }

    return render(
        request,
        'common/index.html',
        context,
    )


def dashboard(request):
    if not get_profile():
        return redirect('index')

    context = {
        'fruits': get_all_fruits(),
        'profile': get_profile(),
    }

    return render(
        request,
        'common/dashboard.html',
        context,
    )
