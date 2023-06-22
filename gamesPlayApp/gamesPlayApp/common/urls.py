from django.urls import path, include
from gamesPlayApp.common.views import dashboard, home_page

urlpatterns = [
    path('', home_page, name='home page'),
    path('dashboard/', dashboard, name='dashboard'),
]
