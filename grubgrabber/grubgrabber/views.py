from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import urllib
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

GOOGLEKEY = open("key.txt").readline()

def index(request):
    return render(request, "index.html")

def search(request):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        #Work in progress
        args = {"searchParam": request.POST["search"]}
        #payload = {"address": urllib.quote_plus(request.POST["search"]), "key": GOOGLEKEY}
        #geocode = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload) #returns 404

        #print geocode.text
        #payload = {"location": urllib.quote_plus(request.POST["search"]), "types":"bakery|cafe|food|meal_takeaway|restaurant" ,"rankby":"distance", "key": GOOGLEKEY}
        #nearbysearch = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=payload)
        #print r.url
        #print r.text
        #args["places"] = nearbysearch.json["results"]
        args["mapsKey"] = GOOGLEKEY
        return render(request, "search.html", args)

def getKey(request):
    return HttpResponse(GOOGLEKEY)

def place(request):
    context_dict = {}
    PLACE_ID = request.GET.get('p', '')
    context_dict['PLACE_ID'] = PLACE_ID
    context_dict["mapsKey"] = GOOGLEKEY
    return render(request, "place.html",context_dict)

@login_required
def register_profile(request):
    registered_profile = False
    context_dict = {}

    if request.method == 'POST':
        try:
            profile = UserProfile.objects.get(user=request.user)
            profile_form = UserProfileForm(request.POST, instance=profile)
        except:
            profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered_profile = True
        else:
            print profile_form.errors
    else:
        profile_form = UserProfileForm()

    context_dict['registered_profile'] = registered_profile
    context_dict['profile_form'] = profile_form

    return render(request, 'register.html', context_dict)

@login_required
def profile(request):
    context_dict = {}
    user = request.user
    context_dict['user'] = user
    try:
        user_profile = UserProfile.objects.get(user=user)
        context_dict['user_profile'] = user_profile
    except:
        pass
    return render(request, 'profile.html', context_dict)
