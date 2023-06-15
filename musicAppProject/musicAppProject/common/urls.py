# common urls

from django.urls import path
from musicAppProject.common.views import index, available_profile_home

urlpatterns = [
    path('', index, name='index'),
    path('home/', available_profile_home, name="available profile home"),

]
