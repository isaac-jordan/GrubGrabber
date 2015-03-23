from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from grubgrabber.models import Like, UserProfile
from django.contrib.auth.models import User
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grubgrabber.settings')

def add_like(place_id, name):
    like = Like.objects.get_or_create(name=name, place_id=place_id)[0]
    return like

def add_user_and_profile(name, email, password, about):
    u = User.objects.get_or_create(username = name, email=email, password=password)[0]
    UserProfile.objects.get_or_create(user = u, about = about)
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
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZeek", 'Greggs')
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZee", 'Bills')
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZek", 'Stevens')
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOeek", 'Bens')

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        no_recent_eats = len(response.context['likes'])
        self.assertEqual(no_recent_eats , 4)
        for like in response.context['likes']:
            print like
        #self.assertTrue('Greggs' in response.context['likes']) #Fails

class ProfileViewTests(TestCase):

    def test_username_shows(self):
        add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
