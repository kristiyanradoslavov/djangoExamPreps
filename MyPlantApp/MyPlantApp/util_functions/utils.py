from django.shortcuts import redirect

from MyPlantApp.users.models import Profile


def get_profile():
    current_account = Profile.objects.all()

    return current_account
