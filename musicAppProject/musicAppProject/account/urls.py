# account urls

from django.urls import path
from musicAppProject.account.views import profile_details, profile_delete

urlpatterns = [
    path('details/', profile_details, name='profile details'),
    path('delete/', profile_delete, name='profile delete'),
]
