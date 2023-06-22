from django.urls import path
from gamesPlayApp.user.views import profile_edit, profile_create, profile_details, profile_delete

urlpatterns = [
    path('create/', profile_create, name='create profile'),
    path('details/', profile_details, name='profile details'),
    path('edit/', profile_edit, name='edit profile'),
    path('delete/', profile_delete, name='delete profile'),
]
