from django.shortcuts import render, redirect

from gamesPlayApp.user.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from gamesPlayApp.util_functions.get_average_rating import get_average_rating
from gamesPlayApp.util_functions.get_games import get_all_games
from gamesPlayApp.util_functions.get_profile import get_profile


def profile_create(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(
        request,
        'user/create-profile.html',
        context,
    )


def profile_details(request):
    if not get_profile():
        return redirect('home page')

    profile = get_profile()
    games_count = len([game for game in get_all_games()])
    rating_sum = sum([game.rating for game in get_all_games()])

    average_rating = get_average_rating(games_count, rating_sum)

    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
    }

    return render(
        request,
        'user/details-profile.html',
        context,
    )


def profile_edit(request):
    if not get_profile():
        return redirect('home page')

    profile = get_profile()

    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(
        request,
        'user/edit-profile.html',
        context,
    )


def profile_delete(request):
    if not get_profile():
        return redirect('home page')

    profile = get_profile()

    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(
        request,
        'user/delete-profile.html',
        context,
    )
