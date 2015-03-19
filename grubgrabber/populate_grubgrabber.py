import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grubgrabber.settings')
import django
django.setup()
from grubgrabber.models import *
from django.contrib.auth.models import User


def populate():
    user1 = add_user('Python','dingodave@gmail.com','dingos')

    add_like(name='Gregs',
        place_id="ChIJ-4qF7s5FiEgR6bRXbXOZeek",
        user = user1)

    add_like(name='Burger King',
        place_id="ChIJWxM5_p9PiEgRAC7To6WEPFA",
        user = user1)

    add_like(name='Taco Mazama',
        place_id="ChIJPbJK8M5FiEgR9efuD8HlDJs",
        user = user1)

    add_like(name='SUBWAY Glasgow',
        place_id="ChIJ3RRg-c5FiEgRnzxq7jiox70",
        user = user1)

    add_like(name='Chunky Chicken',
        place_id="ChIJpavn3ChEiEgRDqLFmr1wJ1U",
        user = user1)

    add_like(name='Tchai-Ovna House of Tea',
        place_id="ChIJWWPdpzJEiEgRdd3UZcKheik",
        user = user1)

    add_blacklist(place_id ="ChIJ-7gDJtYRiEgRhcV1zoFOCXc",
        user = user1)

     #Print out what we have added to the user.
    print "added :)"

def add_user(name, email, password):
    u = User.objects.get_or_create(username = name, email=email, password=password)[0]
    u.save()
    return u

def add_like(name, place_id, user):
    l = Like.objects.get_or_create(name=name, user = user, place_id = place_id)[0]
    l.save()
    return l

def add_blacklist(place_id, user):
    b = Blacklist.objects.get_or_create(place_id = place_id, user = user)
    return b

# Start execution here!
if __name__ == '__main__':
    print "Starting grubber population script..."
    populate()
