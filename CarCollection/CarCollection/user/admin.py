from django.contrib import admin

from CarCollection.user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'age']
