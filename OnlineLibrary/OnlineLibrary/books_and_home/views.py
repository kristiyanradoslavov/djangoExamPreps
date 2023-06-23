from django.shortcuts import render, redirect

from OnlineLibrary.books_and_home.forms import AddBookForm, EditBookForm
from OnlineLibrary.books_and_home.models import Book
from OnlineLibrary.user.forms import CreateProfileForm
from OnlineLibrary.user.models import Profile
from OnlineLibrary.util_functions.get_profile import get_profile


def existing_profile(request, profile):
    context = {
        'profile': profile,
        "books": Book.objects.all(),
    }

    return render(
        request,
        'home_and_books/home-with-profile.html',
        context
    )


def home_page(request):
    profile = get_profile()

    if profile:
        return existing_profile(request, profile)

    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(
        request,
        'home_and_books/home-no-profile.html',
        context,
    )


def book_add(request):
    if request.method == "GET":
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': Profile.objects.get()
    }
    return render(
        request,
        'home_and_books/add-book.html',
        context,
    )


def book_edit(request, book_id):
    current_book = Book.objects.filter(id=book_id).get()

    if request.method == "GET":
        form = EditBookForm(instance=current_book)
    else:
        form = EditBookForm(request.POST, instance=current_book)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'book': current_book,
        'form': form,
        'profile': get_profile()
    }

    return render(
        request,
        'home_and_books/edit-book.html',
        context
    )


def book_details(request, book_id):
    current_book = Book.objects.filter(id=book_id).get()

    context = {
        'book': current_book,
        'profile': get_profile()
    }

    return render(
        request,
        'home_and_books/book-details.html',
        context,
    )


def book_delete(request, book_id):
    current_book = Book.objects.filter(id=book_id).get()
    current_book.delete()

    return redirect('home page')
