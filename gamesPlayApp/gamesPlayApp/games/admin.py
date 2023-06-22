from django.contrib import admin

from gamesPlayApp.games.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
