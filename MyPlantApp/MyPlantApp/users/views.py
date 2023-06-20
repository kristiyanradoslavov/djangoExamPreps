from django.shortcuts import render, redirect

from MyPlantApp.common_and_plants.models import Plant
from MyPlantApp.users.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from MyPlantApp.util_functions.utils import get_profile


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(
        request,
        'users/create-profile.html',
        context
    )


def profile_details(request):
    if not get_profile():
        return redirect('home page')

    profile = get_profile().get()
    plant_count = Plant.objects.all().count()

    context = {
        'profile_exists': profile,
        'plant_count': plant_count
    }
    return render(
        request,
        'users/profile-details.html',
        context
    )


def edit_profile(request):
    if not get_profile():
        return redirect('home page')

    profile = get_profile().get()

    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile_exists': profile,
    }

    return render(
        request,
        'users/edit-profile.html',
        context
    )


def delete_profile(request):
    if not get_profile():
        return redirect('home page')

    profile = get_profile().get()

    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile_exists': profile,
    }

    return render(
        request,
        'users/delete-profile.html',
        context
    )
