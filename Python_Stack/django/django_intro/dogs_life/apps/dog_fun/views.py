from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def nums(request, nums):
    return HttpResponse(f"placeholder to display blog number: {nums}")
def nums_edit(request, nums):
    return HttpResponse(f"placeholder to display blog number: {nums}")
def nums_delete(request, nums):
    return redirect("/")