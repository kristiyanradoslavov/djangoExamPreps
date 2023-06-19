from django.urls import path, include
from MyPlantApp.users.views import profile_details, edit_profile, create_profile, delete_profile

urlpatterns = [
    path('details/', profile_details, name='profile details'),
    path('create/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]
