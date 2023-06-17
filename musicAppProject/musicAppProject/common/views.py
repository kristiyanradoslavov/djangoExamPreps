# common views

from django.shortcuts import render, redirect

from musicAppProject.account.forms import RegistrationForm
from musicAppProject.common.utils import get_account, get_album


def index(request):
    if get_account():
        return available_profile_home(request)

    if request.method == "GET":
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return available_profile_home(request)

    context = {
        'form': form
    }
    return render(request, 'common/home-no-profile.html', context)


def available_profile_home(request):
    if not get_account():
        return redirect(index)

    context = {
        'album': get_album(),
        'profile': get_account(),
    }
    return render(request, 'common/home-with-profile.html', context)
