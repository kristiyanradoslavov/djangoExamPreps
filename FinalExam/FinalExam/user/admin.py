from django.contrib import admin

from FinalExam.user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
