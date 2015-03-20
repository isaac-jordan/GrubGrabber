from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import urllib
import json
from grubgrabber.models import Like, UserProfile, Favourite, Blacklist
from models import Like, UserProfile, Favourite
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from grubgrabber.forms import UserForm, UserProfileForm

GOOGLEKEY = open("key.txt").readline()

def index(request):
    likes = Like.objects.all()[:8:-1]
    context_dict = {'likes' : likes}
    
    favourites = Favourite.objects.all()
    favourite_ids = []
    for this in favourites:
        favourite_ids.append(this.place_id)
        
    favourite_ids.sort(mostfav)
    
    #delete duplicates
    mostfavs =list(set(favourite_ids))
    
    #mostfavs = ['ChIJWxM5_p9PiEgRAC7To6WEPFA']
    top_favs = []
    
   # for i in range (8,0):
        #this = Favourites.objects.select_related().filter(place_id = mostfavs[i])
        #top_favs.append(this)[0]
    context_dict['favourites'] = mostfavs
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
    print request.POST["place"]
    if Favourite.objects.filter(user=request.user, place_id=request.POST["place"]).exists():
        Favourite.objects.filter(user=request.user, place_id=request.POST["place"]).delete()
        return HttpResponse("Removed")
    else:
        Favourite.objects.create(user=request.user, place_id=request.POST["place"], name=request.POST["name"])
        return HttpResponse("Added")

@login_required
def addBlacklist(request):
    print request.POST["place"]
    if Blacklist.objects.filter(user=request.user, place_id=request.POST["place"]).exists():
        Blacklist.objects.filter(user=request.user, place_id=request.POST["place"]).delete()
        return HttpResponse("Removed")
    else:
        Blacklist.objects.create(user=request.user, place_id=request.POST["place"], name=request.POST["name"])
        return HttpResponse("Added")

def addLike(request):
    if request.user.is_authenticated():
        Like.objects.create(user=request.user, place_id=request.POST["place"], name=request.POST["name"])
    else:
        Like.objects.create(place_id=request.POST["place"], name=request.POST["name"])
    return HttpResponse("Like added");

def sort_search_results(request):
    initResults = request.POST.getlist('data')
    user = request.user
    print "Before blacklist " + str(initResults)
    #filter out blacklisted items
    results = remove_blacklist_items(user, initResults)
    print "After blacklist " + str(results)
    #create sortable list of lists [,[place_id, weighting value],[etc.]]
    result_list = []
    for place_id in results:
        result_list.append([place_id,0])
    print "After adding" + str(result_list)
    #apply distance weighting (result_list is sorted by distance at this point)
    for i in range(0,len(result_list)):
        result_list[i][1] += (20 - i)

    print "After distance weighting" + str(result_list)

    favourites = Favourite.objects.all() #One DB call
    if request.user.is_authenticated():
        userFavourites = favourites.filter(user=user).values_list('place_id', flat=True)
    else:
        userFavourites = []
    likes = Like.objects.all()
    for result in result_list:
        if result[0] in userFavourites:
            result[1] += 5 #Add 5 if user has favourited place
        liked = likes.filter(place_id=result[0])
        result[1] += len(liked) #Add number of likes

    print "After weighting " + str(result_list)
    result_list.sort(weighting_compare)

    print "After sorting" + str(result_list)
    resultArray = []
    for result in result_list:
        for i in range(len(initResults)):
            if result[0] == initResults[i]:
                print str(result[0]) + " " + str(initResults[i])
                resultArray.append(i)
                break
    print initResults
    print resultArray

    #Return a list of indices, the index refers to it's position in the original list.
    #[5,4,3,2,1] means "take 5th element of first list, then 4th, then 3rd, etc"
    return JsonResponse({"resultArray": resultArray})

def remove_blacklist_items(user, results):
    returnResults = []
    if user.is_authenticated():
        blacklist = Blacklist.objects.select_related().filter(user=user).values_list('place_id', flat=True)
        for place_id in results:
                if not (place_id in blacklist):
                    returnResults.append(place_id)
        return returnResults
    else:
        return results

def number_of_favourites(place_id):
    favourites = Favourite.objects.all().filter(place_id=place_id)
    return len(favourites)

def favourite_compare(a,b):
    if number_of_favourites(a[0]) >= number_of_favourites(b[0]):
        return 1
    return -1

def mostfav(a,b):
    if number_of_favourites(a) >= number_of_favourites(b):
        return 1
    return -1

def number_of_likes(place_id):
    likes = Like.objects.all().filter(place_id=place_id)
    return len(likes)

def like_compare(a,b):
    if number_of_likes(a[0]) >= number_of_likes(b[0]):
        return 1
    return -1

def weighting_compare(a,b):
    if a[1] >= b[1]:
        return -1
    return 1
