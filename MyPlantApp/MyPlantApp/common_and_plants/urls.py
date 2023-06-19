from django.urls import path, include
from MyPlantApp.common_and_plants.views import home_page, catalogue, plant_delete, plant_edit, plant_create, \
    plant_details

urlpatterns = [
    path('', home_page, name='home page'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', plant_create, name='create plant'),
    path('details/<int:plant_id>/', plant_details, name='plant details'),
    path('delete/<int:plant_id>/', plant_delete, name='delete plant'),
    path('edit/<int:plant_id>/', plant_edit, name='edit plant'),
]
