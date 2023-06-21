from django.shortcuts import render


def car_create(request):
    return render(
        request,
        'car/car-create.html',
    )


def car_details(request, car_id):
    return render(
        request,
        'car/car-details.html',
    )


def car_edit(request, car_id):
    return render(
        request,
        'car/car-edit.html',
    )


def car_delete(request, car_id):
    return render(
        request,
        'car/car-delete.html',
    )
