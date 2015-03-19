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

def sort_search_results(result_dict):
    #filter out blacklisted items
    result_dict = exclude_blacklist_items(result_dict)
    #create sortable list of lists [,[place_id, weighting value],[etc.]]
    result_list = []
    for key in result_dict:
        result_list.append([place_id,0])
    #apply distance weighting
    for i in range(0,len(result_list)):
        result_list[i][1] += (20 - i)

    #sort by number of favourites & apply weighting
    result_list.sort(favourite_compare)
    for i in range(0,len(result_list)):
        result_list[i][1] += (20 - i)
        
    #sort by likes & add weighting
    result_list.sort(like_compare)
    for i in range(0,len(result_list)):
        result_list[i][1] += (20 - i)

    #sort by weighted values and return (only prints at teh moment, dont know what type to return?)
    result_list.sort(weighting_compare)
    for i in range(0,len(result_list)):
        print result_list[i][0]
        
    return result_dict

def search(request):
    ########the simple search algorithm#####
    #get 20 nearest items
    #exclude ones in blacklist
    #sort by favourites
    #return results

    ######the not so simple search algorithm#####
    # get nearest 20 items
    # exclude blacklist
    # asign weighting variable to each ( first =20, 2nd = 19, etc.) (maybe implemented)
    # sort by most favourited (first =20, 2nd =19, etc.) (maybe implemented)
    # sort by most liked (same as about) (maybe implemented)
    # sort by most blacklisted (same as above but -) (not implemented)
    # sort by most disliked (same as about but -)
    
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
        favourites = Favourite.objects.select_related().filter(user=user)
        context_dict['favourites'] = favourites
        likes = Like.objects.select_related().filter(user=user)
        context_dict['likes'] = likes
        blacklist = Blacklist.objects.select_related().filter(user=user)
        context_dict['blacklist'] = blacklist
        user_profile = UserProfile.objects.get(user=user)
        context_dict['user_profile'] = user_profile
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

def exclude_blacklist_items(result_dict):
    user = request.user
    blacklist = Blacklist.objects.select_related().filter(user=user)
    for place_id in result_dict:
        for not_here in blacklist:
            if place_id == not_here.place_id:
                del result_dict['place_id']

    return result_dict

def number_of_favourites(place_id):
    favourites = Favourite.objects.all().filter(place_id=place_id)
    return len(favourites)

def favourite_compare(a,b):
    if number_of_favourites(a[0]) >= number_of_favourites(b[0]):
        return 1
    else:
        return -1

def number_of_likes(place_id):
    likes = Like.objects.all().filter(place_id=place_id)
    return len(likes)

def like_compare(a,b):
    if number_of_likes(a[0]) >= number_of_likes(b[0]):
        return 1
    else:
        return -1

def weighting_compare(a,b):
    if a[1] >= b[1]:
        return 1
    else:
        return -1
