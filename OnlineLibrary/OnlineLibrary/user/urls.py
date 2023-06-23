from django.urls import path, include

from OnlineLibrary.user.views import profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('edit/', profile_edit, name='edit profile'),
    path('delete/', profile_delete, name='profile delete'),
]
