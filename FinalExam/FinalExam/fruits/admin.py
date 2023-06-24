from django.contrib import admin

from FinalExam.fruits.models import Fruit


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass
