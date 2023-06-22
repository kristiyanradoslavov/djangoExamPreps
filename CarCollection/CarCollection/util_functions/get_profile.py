from CarCollection.user.models import Profile


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile

    except Profile.DoesNotExist:
        return None

