from math import floor


def get_all_available_genres():
    genre_all_choices = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ]

    return genre_all_choices


def floor_float_number(number):
    return floor(number)

