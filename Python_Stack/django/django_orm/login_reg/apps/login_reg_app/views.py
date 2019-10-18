from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    context = {"home": User.objects.all()}
    return render(request, "login_reg_app/index_start.html", context)

def add_new_user(request):
    context = {"users": User.objects.all()}
    return render(request, "login_reg_app/index_success.html", context)

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
        request.session['user_id'] = newly_created_user
    return redirect("/add_new_user_successful/"+str(newly_created_user.id))

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/add_new_user_successful/'+str(user.id))

def view_user(request, user_id):
    context = {
        "users": User.objects.all(),
    }
    return render(request, "login_reg_app/index_complete.html", context)