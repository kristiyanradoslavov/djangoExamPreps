from django.contrib import admin

from CarCollection.car.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'model', 'year', 'price']
