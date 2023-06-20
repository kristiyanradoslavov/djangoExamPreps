from django.shortcuts import render, redirect

from MyPlantApp.common_and_plants.forms import CreatePlantForm, EditPlantForm, DeletePlantForm
from MyPlantApp.common_and_plants.models import Plant
from MyPlantApp.util_functions.utils import get_profile


def home_page(request):
    context = {
        'profile_exists': get_profile()
    }
    return render(
        request,
        'common/home-page.html',
        context
    )


def catalogue(request):
    if not get_profile():
        return redirect('home page')

    all_plants = Plant.objects.all()

    context = {
        'profile_exists': get_profile(),
        'plants': all_plants
    }

    return render(
        request,
        'common/catalogue.html',
        context
    )


def plant_create(request):
    if not get_profile():
        return redirect('home page')

    if request.method == "GET":
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile_exists': get_profile()
    }

    return render(
        request,
        'plants/create-plant.html',
        context
    )


def plant_details(request, plant_id):
    if not get_profile():
        return redirect('home page')

    current_plant = Plant.objects.filter(pk=plant_id).get()

    context = {
        'plant': current_plant,
        'profile_exists': get_profile(),
    }

    return render(
        request,
        'plants/plant-details.html',
        context
    )


def plant_edit(request, plant_id):
    if not get_profile():
        return redirect('home page')

    plant = Plant.objects.filter(pk=plant_id).get()

    if request.method == "GET":
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile_exists': get_profile(),
        'plant': plant
    }

    return render(
        request,
        'plants/edit-plant.html',
        context
    )


def plant_delete(request, plant_id):
    if not get_profile():
        return redirect('home page')

    plant = Plant.objects.filter(pk=plant_id).get()

    if request.method == "GET":
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile_exists': get_profile(),
    }
    return render(
        request,
        'plants/delete-plant.html',
        context,
    )
