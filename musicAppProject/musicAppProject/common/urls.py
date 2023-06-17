# common urls

from django.urls import path
from musicAppProject.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
