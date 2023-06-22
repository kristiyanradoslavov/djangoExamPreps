from django.shortcuts import render, redirect

from gamesPlayApp.games.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesPlayApp.util_functions.get_games import get_game
from gamesPlayApp.util_functions.get_profile import get_profile


def game_create(request):
    if not get_profile():
        return redirect('home page')

    if request.method == "GET":
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(
        request,
        'games/create-game.html',
        context,
    )


def game_details(request, game_id):
    current_game = get_game(game_id)

    context = {
        'game': current_game,
        'profile': get_profile()
    }

    return render(
        request,
        'games/details-game.html',
        context
    )


def game_edit(request, game_id):
    if not get_profile():
        return redirect('home page')

    current_game = get_game(game_id)

    if request.method == "GET":
        form = EditGameForm(instance=current_game)
    else:
        form = EditGameForm(request.POST, instance=current_game)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        'form': form,
        'profile': get_profile(),
        'game': current_game,
    }
    return render(
        request,
        'games/edit-game.html',
        context,
    )


def game_delete(request, game_id):
    if not get_profile():
        return redirect('home page')

    current_game = get_game(game_id)

    if request.method == "GET":
        form = DeleteGameForm(instance=current_game)
    else:
        form = DeleteGameForm(request.POST, instance=current_game)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        'form': form,
        'profile': get_profile(),
        'game': current_game,
    }

    return render(
        request,
        'games/delete-game.html',
        context,
    )
