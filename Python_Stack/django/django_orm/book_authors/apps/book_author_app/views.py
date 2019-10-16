from django.shortcuts import render, redirect
from .models import Author, Book

def index(request):
    context = {"home": Author.objects.all()}
    return render(request, "book_author_app/index_books_authors.html", context)

def add_new_book(request):
    context = {"books": Book.objects.all()}
    return render(request, "book_author_app/index_add_book.html", context)

def create_book(request):
    if request.method == "POST":
        newly_created_book = Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
        newly_created_book.save()
        return redirect("/view_book/"+str(newly_created_book.id))

def view_book(request, book_id):
    context = {"book": Book.objects.get(id=book_id)}
    return render(request, "book_author_app/index_view_book.html", context)

def add_new_author(request):
    context = {"authors": Author.objects.all()}
    return render(request, "book_author_app/index_add_author.html", context)

def create_author(request):
    if request.method == "POST":
        newly_created_author = Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], notes=request.POST['notes'])
        newly_created_author.save()
        return redirect("/view_author/"+str(newly_created_author.id))

def view_author(request, author_id):
    context = {"author": Author.objects.get(id=author_id)}
    return render(request, "book_author_app/index_view_author.html", context)
    