from django.shortcuts import render

from gamesPlayApp.util_functions.get_games import get_all_games
from gamesPlayApp.util_functions.get_profile import get_profile


def home_page(request):
    context = {
        'profile': get_profile()
    }

    return render(
        request,
        'common/home-page.html',
        context,
    )


def dashboard(request):
    games = get_all_games()

    context = {
        'games': games,
        'profile': get_profile(),
    }

    return render(
        request,
        'common/dashboard.html',
        context,
    )
