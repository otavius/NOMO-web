from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, "app/home.html")

def what_we_do_page(request):
    return render(request, "app/what-we-do.html")
    