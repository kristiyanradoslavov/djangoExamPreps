# common urls

from django.urls import path
from musicAppProject.common.views import home_page

urlpatterns = [
    path('', home_page, name='home page')
]