from django.shortcuts import render


def user_create(request):
    return render(
        request,
        'user/profile-create.html',
    )


def user_details(request):
    return render(
        request,
        'user/profile-details.html',
    )


def user_edit(request):
    return render(
        request,
        'user/profile-edit.html',
    )


def user_delete(request):
    return render(
        request,
        'user/profile-delete.html',
    )
