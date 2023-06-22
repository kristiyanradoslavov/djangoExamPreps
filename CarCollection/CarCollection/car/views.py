from django.shortcuts import render, redirect

from CarCollection.car.forms import CreateCarForm, EditCarForm, DeleteCarForm
from CarCollection.util_functions.get_cars import get_cars
from CarCollection.util_functions.get_profile import get_profile


def car_create(request):
    if not get_profile():
        return redirect('index')

    if request.method == "GET":
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(
        request,
        'car/car-create.html',
        context,
    )


def car_details(request, car_id):
    if not get_profile():
        return redirect('index')

    current_car = get_cars(car_id)

    context = {
        'car': current_car,
        'profile': get_profile(),
    }

    return render(
        request,
        'car/car-details.html',
        context,
    )


def car_edit(request, car_id):
    if not get_profile():
        return redirect('index')

    current_car = get_cars(car_id)

    if request.method == "GET":
        form = EditCarForm(instance=current_car)
    else:
        form = EditCarForm(request.POST, instance=current_car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile(),
        'car': current_car,
    }

    return render(
        request,
        'car/car-edit.html',
        context,
    )


def car_delete(request, car_id):
    if not get_profile():
        return redirect('index')

    current_car = get_cars(car_id)

    if request.method == "GET":
        form = DeleteCarForm(instance=current_car)
    else:
        form = DeleteCarForm(request.POST, instance=current_car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile(),
        'car': current_car,
    }

    return render(
        request,
        'car/car-delete.html',
        context,
    )
