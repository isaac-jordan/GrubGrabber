from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import urllib
import json
from grubgrabber.models import Like, UserProfile, Favourite, Blacklist
from models import Like, UserProfile, Favourite
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from grubgrabber.forms import UserForm, UserProfileForm

GOOGLEKEY = open("key.txt").readline()

def index(request):
    likes = Like.objects.all()[:8]
    context_dict = {'likes' : likes}
    return render(request, "index.html", context_dict)

def search(request):
    context_dict = {}
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        args = {"searchParam": request.POST["search"]}
        args["mapsKey"] = GOOGLEKEY
        return render(request, "search.html", args)

def getKey(request):
    return HttpResponse(GOOGLEKEY)

def place(request, SEARCH_LOC, PLACE_ID):
    args = {}
    print SEARCH_LOC
    args['SEARCH_LOC'] = SEARCH_LOC
    args['PLACE_ID'] = PLACE_ID
    args["mapsKey"] = GOOGLEKEY

    return render(request, "place.html", args)

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

    return render(request, 'registration/profile_registration.html', context_dict)

@login_required
def profile(request):
    context_dict = {}
    user = request.user
    context_dict['user'] = user
    try:
        user_profile = UserProfile.objects.get(user=user)
        context_dict['user_profile'] = user_profile
        favourites = Favourite.objects.select_related().filter(user=user)
        context_dict['favourites'] = favourites
        likes = Like.objects.select_related().filter(user=user)
        context_dict['likes'] = likes
        blacklist = Blacklist.objects.select_related().filter(user=user)
        context_dict['blacklist'] = blacklist
    except:
        pass
    return render(request, 'profile.html', context_dict)

@login_required
def addFavourite(request):
    print request.GET["place"]
    if Favourite.objects.filter(user=request.user, place_id=request.GET["place"]).exists():
        Favourite.objects.filter(user=request.user, place_id=request.GET["place"]).delete()
        return HttpResponse("Removed")
    else:
        Favourite.objects.create(user=request.user, place_id=request.GET["place"])
        return HttpResponse("Added")

@login_required
def addBlacklist(request):
    print request.GET["place"]
    if Blacklist.objects.filter(user=request.user, place_id=request.GET["place"]).exists():
        Blacklist.objects.filter(user=request.user, place_id=request.GET["place"]).delete()
        return HttpResponse("Removed")
    else:
        Blacklist.objects.create(user=request.user, place_id=request.GET["place"])
        return HttpResponse("Added")
