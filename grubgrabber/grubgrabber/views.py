from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib
import json

GOOGLEKEY = open("key.txt").readline()

def index(request):
    return render(request, "index.html")

def search(request):
    if request.method == "GET":
        return index(request)
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

def place(request, PLACE_ID):
    return render(request, "place.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    context_dict = {}
    user = request.user
    context_dict['user'] = user
    return render(request, 'profile.html', context_dict)
