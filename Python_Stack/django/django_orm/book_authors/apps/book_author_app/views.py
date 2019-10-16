from django.shortcuts import render, redirect
from .models import Author

def index(request):
    context = {"authors": Author.objects.all()}
    return render(request, "book_author_app/index_books_authors.html", context)

def view_book(request):
    context = {"authors": Author.objects.all()}
    return render(request, "book_author_app/index_view_book.html", context)

def add_new_book(request):
    context = {"authors": Author.objects.all()}
    return render(request, "book_author_app/index_add_book.html", context)

def view_author(request):
    context = {"authors": Author.objects.all()}
    return render(request, "book_author_app/index_view_author.html", context)

def add_new_author(request):
    context = {"authors": Author.objects.all()}
    return render(request, "book_author_app/index_add_author.html", context)
