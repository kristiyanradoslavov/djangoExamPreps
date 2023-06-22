from gamesPlayApp.games.models import Game


def get_all_games():
    game = Game.objects.all()
    return game


def get_game(game_id):
    game = Game.objects.filter(id=game_id).get()
    return game
