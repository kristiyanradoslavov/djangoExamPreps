from django.shortcuts import render, redirect

from OnlineLibrary.user.forms import EditProfileForm, DeleteProfileForm
from OnlineLibrary.util_functions.get_profile import get_profile


def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(
        request,
        'users/profile.html',
        context,
    )


def profile_edit(request):
    profile = get_profile()

    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile
    }

    return render(
        request,
        'users/edit-profile.html',
        context,
    )


def profile_delete(request):
    profile = get_profile()

    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile
    }

    return render(
        request,
        'users/delete-profile.html',
        context,
    )
