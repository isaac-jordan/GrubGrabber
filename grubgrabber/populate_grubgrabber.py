import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grubgrabber.settings')
import django
from grubgrabber.models import User, Favourite, Like, Dislike, Blacklist, UserProfile
from django.contrib.auth.models import User

django.setup()

def populate():
    user1 = add_user('DingoDave','dingodave@gmail.com','dingos',
        'My name is Dave! I love to eat & dingos are my favourite animals')

    user2 = add_user('Python','snakeboy@snakemail.com','snakey',
                     'How does this thing work?')

    user3 = add_user('Estebar','hotboy89@gmail.com','chickens12',
                     'Hola amigos')

    user4 = add_user('Moleman','reallyunderground@yahoomail.com','tunneling',
                     'average foodie consumer by day, mole by night')

    user5 = add_user('test','test@gmail.com','test', 'test description')

    user5 = add_user('JessicaRabbit','bugsywoman@gmail.com','rogerroger1',
                     'Hey people!')

    user6 = add_user('AnonFooder','73359000@haxormail.com','grabbagrabba',
                     'Who am i?')

    add_like(name='Greggs',
        place_id="ChIJ-4qF7s5FiEgR6bRXbXOZeek",
        user = user1)

    add_like(name='Burger King',
        place_id="ChIJWxM5_p9PiEgRAC7To6WEPFA",
        user = user1)

    add_blacklist(name='Burger King',
        place_id="ChIJWxM5_p9PiEgRAC7To6WEPFA",
        user = user4)

    add_dislike(name='Burger King',
        place_id="ChIJWxM5_p9PiEgRAC7To6WEPFA",
        user = user4)

    add_dislike(name='Burger King',
        place_id="ChIJWxM5_p9PiEgRAC7To6WEPFA",
        user = user5)

    add_dislike(name='Burger King',
        place_id="ChIJWxM5_p9PiEgRAC7To6WEPFA",
        user = user3)

    add_like(name='Taco Mazama',
        place_id="ChIJPbJK8M5FiEgR9efuD8HlDJs",
        user = user1)

    add_like(name='Taco Mazama',
        place_id="ChIJPbJK8M5FiEgR9efuD8HlDJs",
        user = user6)

    add_favourite(name='Taco Mazama',
        place_id="ChIJPbJK8M5FiEgR9efuD8HlDJs",
        user = user6)

    add_like(name='SUBWAY Glasgow',
        place_id="ChIJ3RRg-c5FiEgRnzxq7jiox70",
        user = user1)

    add_like(name='Chunky Chicken',
        place_id="ChIJpavn3ChEiEgRDqLFmr1wJ1U",
        user = user1)

    add_favourite(name='Chunky Chicken',
        place_id="ChIJpavn3ChEiEgRDqLFmr1wJ1U",
        user = user5)

    add_favourite(name='Chunky Chicken',
        place_id="ChIJpavn3ChEiEgRDqLFmr1wJ1U",
        user = user1)

    add_like(name='Chunky Chicken',
        place_id="ChIJpavn3ChEiEgRDqLFmr1wJ1U",
        user = user5)

    add_like(name='Tchai-Ovna House of Tea',
        place_id="ChIJWWPdpzJEiEgRdd3UZcKheik",
        user = user1)

    add_favourite(name='Tchai-Ovna House of Tea',
        place_id="ChIJWWPdpzJEiEgRdd3UZcKheik",
        user = user1)

    add_favourite(name='Tchai-Ovna House of Tea',
        place_id="ChIJWWPdpzJEiEgRdd3UZcKheik",
        user = user4)

    add_like(name='Tchai-Ovna House of Tea',
        place_id="ChIJWWPdpzJEiEgRdd3UZcKheik",
        user = user4)

    add_like(name='Tchai-Ovna House of Tea',
        place_id="ChIJWWPdpzJEiEgRdd3UZcKheik",
        user = user5)

    add_like(name='Casa De Emanuel',
        place_id="ChIJtdOXLpgWNIgRDGGwgem5LeM",
        user = user3)

    add_dislike(place_id ="ChIJ-7gDJtYRiEgRhcV1zoFOCXc",
        user = user1,
        name = 'Stravaigin')

    add_blacklist(place_id ="ChIJ-7gDJtYRiEgRhcV1zoFOCXc",
        user = user1,
        name = 'Stravaigin')

    add_blacklist(place_id ="ChIJ-7gDJtYRiEgRhcV1zoFOCXc",
        user = user5,
        name = 'Stravaigin')

    add_blacklist(place_id ="ChIJNanQ24gWNIgRcPYC9_6WjMg",
        user = user3,
        name = 'Sunoco Gas Station')

    add_blacklist(place_id ="ChIJnb2R1WEWNIgREjlN5fz-DvM",
        user = user3,
        name = 'China City')

    add_like(name='Golden House',
        place_id="ChIJsdnAPBQOhEgRdgHGBNtfQ5A",
        user = user6)

    add_favourite(name='Golden House',
        place_id="ChIJsdnAPBQOhEgRdgHGBNtfQ5A",
        user = user6)

    add_dislike(name='Golden House',
        place_id="ChIJsdnAPBQOhEgRdgHGBNtfQ5A",
        user = user4)

    add_like(name="Rabbie's Cafe",
        place_id="ChIJI5r8_o7Hh0gRc9Mu8QJaRkU",
        user = user2)

    add_favourite(name="Rabbie's Cafe",
        place_id="ChIJI5r8_o7Hh0gRc9Mu8QJaRkU",
        user = user5)

    add_dislike(name="Rabbie's Cafe",
        place_id="ChIJI5r8_o7Hh0gRc9Mu8QJaRkU",
        user = user1)

    add_like(name="Peking House",
        place_id="ChIJrbtxVQpFiEgRvrJqYAodSHc",
        user = user5)

    add_dislike(name="Peking House",
        place_id="ChIJrbtxVQpFiEgRvrJqYAodSHc",
        user = user4)

    add_blacklist(name="Peking House",
        place_id="ChIJrbtxVQpFiEgRvrJqYAodSHc",
        user = user4)

    add_dislike(name="Peking House",
        place_id="ChIJrbtxVQpFiEgRvrJqYAodSHc",
        user = user3)

    add_like(name="Ciao Roma",
        place_id="ChIJ-4Cj-47Hh0gRYiyFHXYXfnk",
        user = user2)

    add_favourite(name="Ciao Roma",
        place_id="ChIJ-4Cj-47Hh0gRYiyFHXYXfnk",
        user = user2)

    add_dislike(name="HongFu Noodlebar",
        place_id="ChIJB8vd-47Hh0gRf7RQHkpN9LM",
        user = user2)

    add_like(name="HongFu Noodlebar",
        place_id="ChIJB8vd-47Hh0gRf7RQHkpN9LM",
        user = user4)

    add_favourite(name="HongFu Noodlebar",
        place_id="ChIJB8vd-47Hh0gRf7RQHkpN9LM",
        user = user4)

     #Print out what we have added to the user.
    print "added :)"

def add_user(name, email, password, about):
    u = User.objects.create_user(name, email,password)
    u.save()
    UserProfile.objects.get_or_create(user = u, about = about, locations_json="{}")
    return u

def add_like(name, place_id, user):
    l = Like.objects.get_or_create(name=name, user = user, place_id = place_id)[0]
    l.save()
    return l

def add_blacklist(place_id, user, name):
    b = Blacklist.objects.get_or_create(place_id = place_id, user = user, name = name)[0]
    return b

def add_dislike(place_id, user, name):
    d = Dislike.objects.get_or_create(place_id = place_id, user = user, name = name)[0]
    return d

def add_favourite(place_id,user,name):
    f = Favourite.objects.get_or_create(place_id = place_id, user = user, name = name)[0]
    return f

# Start execution here!
if __name__ == '__main__':
    print "Starting grubber population script..."
    populate()
