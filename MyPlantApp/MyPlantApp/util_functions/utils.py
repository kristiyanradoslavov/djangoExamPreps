from MyPlantApp.users.models import Profile


def get_profile():
    current_account = Profile.objects.all()

    return current_account
