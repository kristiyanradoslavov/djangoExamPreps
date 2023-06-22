from django.contrib import admin

from gamesPlayApp.user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'age']
