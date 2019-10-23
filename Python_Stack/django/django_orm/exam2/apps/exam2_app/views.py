from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    context = {"home": User.objects.all()}
    return render(request, "exam2_app/login_reg.html", context)

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

def add_new_user_successful(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "users" : User.objects.all()
    }
    return render(request, "exam2_app/welcome.html", context)

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/dashboard')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "jobs" : Job.objects.all(),
    }
    return render(request, "exam2_app/dashboard.html", context)

def add_job_form(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "jobs" :Job.objects.all(),
    }
    return render(request, "exam2_app/new_job.html", context)

def create_job(request):
    if request.method == "POST":
        errors = Job.objects.validate_job(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_job_form')
        job = Job.objects.create(title= request.POST['title'], description= request.POST['description'], location= request.POST['location'])
        return redirect("/add_job_form")

def add_job_save(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return redirect("/create_job/")

def edit_job_form(request, id):
    context = {
        "job": Job.objects.get(id=id),
    }
    return render(request, "exam2_app/edit_job.html", context)

def edit_job(request, id):
    if request.method == "POST":
        errors = Job.objects.validate_job(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/jobs/edit_form/"+id)
        edit = Job.objects.get(id=id)
        edit.title = request.POST["title"]
        edit.location = request.POST["location"]
        edit.description = request.POST["description"]
        edit.save()
        return redirect("/dashboard")

def view_job(request, id):
    context = {
        "job": Job.objects.get(id=id),
    }
    return render(request, "exam2_app/view_job.html", context)

def remove_job(request, id):
    remove = Job.objects.get(id=id)
    remove.delete()
    return redirect("/dashboard")
