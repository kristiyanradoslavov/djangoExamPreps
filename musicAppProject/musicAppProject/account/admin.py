from django.contrib import admin
from musicAppProject.account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "age"]
