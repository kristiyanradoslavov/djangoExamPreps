from django.core.exceptions import ObjectDoesNotExist

from musicAppProject.account.models import Profile
from musicAppProject.album.models import Album


def get_account():
    from django.forms import models
    try:
        account = Profile.objects.get()
        return account
    except ObjectDoesNotExist:
        return None


def get_album():
    album = Album.objects.all()

    if album:
        return album

    else:
        return None
