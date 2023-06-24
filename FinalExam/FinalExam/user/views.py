from django.shortcuts import render, redirect

from FinalExam.user.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from FinalExam.util_functions.get_fruits import get_all_fruits
from FinalExam.util_functions.get_profile import get_profile


def profile_create(request):
    if get_profile():
        return redirect('index')

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(
        request,
        'users/create-profile.html',
        context,
    )


def profile_details(request):
    if not get_profile():
        return redirect('index')

    number_of_posts = len(get_all_fruits())

    context = {
        'profile': get_profile(),
        'total_posts': number_of_posts,
    }

    return render(
        request,
        'users/details-profile.html',
        context,
    )


def profile_edit(request):
    if not get_profile():
        return redirect('index')

    current_profile = get_profile()

    if request.method == "GET":
        form = EditProfileForm(instance=current_profile)
    else:
        form = EditProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(
        request,
        'users/edit-profile.html',
        context,
    )


def profile_delete(request):
    if not get_profile():
        return redirect('index')

    current_profile = get_profile()

    if request.method == "GET":
        form = DeleteProfileForm(instance=current_profile)
    else:
        form = DeleteProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(
        request,
        'users/delete-profile.html',
        context,
    )
