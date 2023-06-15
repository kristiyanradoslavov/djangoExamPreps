from musicAppProject.account.models import Profile
from musicAppProject.album.models import Album


def get_account():
    account = Profile.objects.all()

    if account:
        return account
    else:
        return None


def get_album():
    album = Album.objects.all()

    if album:
        return album

    else:
        return None
