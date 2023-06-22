from django.urls import path, include
from gamesPlayApp.games.views import game_create, game_details, game_edit, game_delete

urlpatterns = [
    path('create/', game_create, name='create game'),
    path('details/<int:game_id>/', game_details, name='game details'),
    path('edit/<int:game_id>/', game_edit, name='edit game'),
    path('delete/<int:game_id>/', game_delete, name='delete game'),
]
