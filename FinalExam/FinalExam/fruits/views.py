from django.shortcuts import render, redirect

from FinalExam.fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from FinalExam.util_functions.get_fruits import get_fruit
from FinalExam.util_functions.get_profile import get_profile


def fruit_create(request):
    if not get_profile():
        return redirect('index')

    if request.method == 'GET':
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(
        request,
        'fruits/create-fruit.html',
        context,
    )


def fruit_details(request, fruit_id):
    if not get_profile():
        return redirect('index')

    current_fruit = get_fruit(fruit_id)

    context = {
        'profile': get_profile(),
        'fruit': current_fruit
    }

    return render(
        request,
        'fruits/details-fruit.html',
        context,
    )


def fruit_edit(request, fruit_id):
    if not get_profile():
        return redirect('index')

    current_fruit = get_fruit(fruit_id)

    if request.method == 'GET':
        form = EditFruitForm(instance=current_fruit)
    else:
        form = EditFruitForm(request.POST, instance=current_fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile(),
        'fruit': current_fruit,
    }

    return render(
        request,
        'fruits/edit-fruit.html',
        context,
    )


def fruit_delete(request, fruit_id):
    if not get_profile():
        return redirect('index')

    current_fruit = get_fruit(fruit_id)

    if request.method == 'GET':
        form = DeleteFruitForm(instance=current_fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=current_fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile(),
        'fruit': current_fruit,
    }

    return render(
        request,
        'fruits/delete-fruit.html',
        context
    )
