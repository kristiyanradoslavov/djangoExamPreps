from django.shortcuts import render, redirect

from MyPlantApp.users.forms import CreateProfileForm


def profile_details(request):
    return render(
        request,
        'users/profile-details.html',
    )


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


def edit_profile(request):
    return render(
        request,
        'users/edit-profile.html',
    )


def delete_profile(request):
    return render(
        request,
        'users/delete-profile.html',
    )

