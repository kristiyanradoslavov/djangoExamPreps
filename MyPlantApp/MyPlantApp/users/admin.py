from django.contrib import admin

from MyPlantApp.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'first_name', 'last_name']
