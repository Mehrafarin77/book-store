from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Avg

# Create your views here.
def view_books(request):
    books = Book.objects.all().order_by('title')
    books_count = books.count()
    books_rating_avg = books.aggregate(Avg('rating'))
    context = {
        'books': books,
        'count': books_count,
        'rating_avg': books_rating_avg.get('rating__avg', 1)
    }
    return render(request, 'view_books.html', context)

def view_book(request, slug):
    try:
        book = Book.objects.get(slug=slug)
        context = {
            'book': book
        }
        return render(request, 'view_book.html', context)
    except:
        raise Http404()

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_outlet:view_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form':form})

def delete_book(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return HttpResponseRedirect(reverse('book_outlet:view_books'))

def edit_book(request, id):
    book = Book.objects.get(pk=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(f'/books/{id}')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_outlet:add_book')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_outlet:add_book')
    else:
        form = AddressForm()
    return render(request, 'add_address.html', {'form':form})


def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_outlet:add_book')
    else:
        form = CountryForm()
    return render(request, 'add_country.html', {'form':form})










