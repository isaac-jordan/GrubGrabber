from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def search(request):
    return render(request, "search.html")

def place(request, PLACE_ID):
    return render(request, "place.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")
