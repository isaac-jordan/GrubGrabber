from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from grubgrabber.models import Like, UserProfile
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
        print response
        self.assertEqual(response.status_code, 200)
        likes = []
        for like in response.context['likes']:
            likes.append(like.name)

        no_recent_eats = len(likes)
        self.assertEqual(no_recent_eats , 4)
        self.assertTrue('Greggs' in likes)
        self.assertTrue('Bills' in likes)
        self.assertTrue('Stevens' in likes)
        self.assertTrue('Bens' in likes)

class ProfileViewTests(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_username_shows(self):
        add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "stevo")

class LogInViewTests(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_username_shows(self):
        response = self.client.get("/accounts/login")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please sign in")

class UserProfileTests(TestCase):

    def test_locations_json(self):
        user = add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        profile = UserProfile.objects.filter(user=user)[0]
        self.assertTrue(json.loads(profile.locations_json) == {})

    def test_user(self):
        user = add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        profile = UserProfile.objects.filter(user=user)[0]
        self.assertTrue(user.email == "stevo@gmail.com")
        self.assertTrue(user.username == "stevo")

    def test_user_profile(self):
        user = add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        profile = UserProfile.objects.filter(user=user)[0]
        self.assertTrue(profile.about == "howdy")
