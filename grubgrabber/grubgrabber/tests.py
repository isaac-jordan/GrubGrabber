from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from grubgrabber.models import Like, Favourite, Blacklist, UserProfile
from django.contrib.auth.models import User
import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grubgrabber.settings')

def add_like(place_id, name, user=None):
    like = Like.objects.get_or_create(user=user, name=name, place_id=place_id)[0]
    return like

def add_user_and_profile(name, email, password, about):
    u = User.objects.get_or_create(username = name, email=email, password=password)[0]
    UserProfile.objects.get_or_create(user = u, about = about, locations_json=json.dumps({}))
    return u

class IndexViewTests(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index_view_with_no_recent_eats(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recent eats")

    def test_index_view_with_recent_eats(self):
        u = add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZeek", 'Greggs', u)
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZee", 'Bills', u)
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZek", 'Stevens', u)
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOeek", 'Bens', u)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        no_recent_eats = len(response.context['likes'])
        self.assertEqual(no_recent_eats , 4)
        likes = []
        for like in response.context['likes']:
            likes.append(like.name)
        self.assertTrue('Greggs' in likes)

class ProfileViewTests(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_username_shows(self):
        add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class FavouriteTests(TestCase):
    pass

class BlacklistTests(TestCase):
    pass

class UserProfileTests(TestCase):

    def test_locations_json(self):
        user = add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        profile = UserProfile.objects.filter(user=user)[0]
        self.assertTrue(json.loads(profile.locations_json) == {})
