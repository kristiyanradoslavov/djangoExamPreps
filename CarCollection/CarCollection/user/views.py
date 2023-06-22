from django.shortcuts import render, redirect

from CarCollection.user.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from CarCollection.util_functions.get_cars import get_cars
from CarCollection.util_functions.get_profile import get_profile


def user_create(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(
        request,
        'user/profile-create.html',
        context,
    )


def user_details(request):
    if not get_profile():
        return redirect('index')

    total_price = sum([car.price for car in get_cars()])

    context = {
        'profile': get_profile(),
        'total_price': total_price,
    }

    return render(
        request,
        'user/profile-details.html',
        context,
    )


def user_edit(request):
    if not get_profile():
        return redirect('index')

    current_user = get_profile()

    if request.method == "GET":
        form = EditProfileForm(instance=current_user)
    else:
        form = EditProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('user details')

    context = {
        'form': form,
        'profile': current_user,
    }

    return render(
        request,
        'user/profile-edit.html',
        context,
    )


def user_delete(request):
    if not get_profile():
        return redirect('index')

    current_user = get_profile()

    if request.method == "GET":
        form = DeleteProfileForm(instance=current_user)
    else:
        form = DeleteProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('user details')

    context = {
        'form': form,
        'profile': current_user,
    }

    return render(
        request,
        'user/profile-delete.html',
        context,
    )
