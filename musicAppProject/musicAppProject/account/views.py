# account views

from django.shortcuts import render


def profile_details(request):
    return render(request, 'account/profile-details.html')


def profile_delete(request):
    return render(request, 'account/profile-delete.html')


