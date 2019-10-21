from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    context = {"home": User.objects.all()}
    return render(request, "exam_app/login_reg.html", context)

#def view_author(request, author_id):
#    context = {
#        "author": Author.objects.get(id=author_id),
#        'books': Book.objects.all(),
#    }
#    return render(request, "book_author_app/#index_view_author.html", context)

def add_new_user_successful(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "users" : User.objects.all()
    }
    return render(request, "exam_app/welcome.html", context)

def user_home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, "exam_app/dashboard.html", context)

def add_trip_form(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return render(request, "exam_app/new_trip.html", context)

def add_trip_save(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return redirect("/create_trip/"+str(user.id))

def create_user(request):
    if request.method == "POST":
        errors = User.objects.validate_reg(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        newly_created_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        request.session['user_id'] = newly_created_user.id
    return redirect("/add_new_user_successful")

def logout(request):
    del request.session['user_id']
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/user_home')

#def new_user(request, user_id):
#    context = {
#        "users": User.objects.all(),
#    }
#    return render(request, "exam_app/welcome.html", context)