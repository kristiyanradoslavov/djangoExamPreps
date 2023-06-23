from django.contrib import admin

from OnlineLibrary.user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
