from django.contrib import admin

from MyPlantApp.common_and_plants.models import Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['pk', 'plant_type', 'name', 'price']
