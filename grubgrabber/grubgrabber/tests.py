from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from grubgrabber.models import Like
from django.contrib.auth.models import User
from django.test.utils import setup_test_environment

setup_test_environment()

def add_like(place_id, name):
    like = Like.objects.get_or_create(name=name, place_id=place_id)[0]
    like.save()
    return like
    
def add_user_and_profile(name, email, password, about):
    u = User.objects.get_or_create(username = name, email=email, password=password)[0]
    u.save()
    UserProfile.objects.get_or_create(user = u, about = about)
    return u
    

class IndexViewTests(TestCase):

    def test_index_view_with_no_recent_eats(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recent eats")
		
    def test_index_view_with_recent_eats(self):
    
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZeek", 'Greggs')
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZeek", 'Bills')
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZeek", 'Stevens')
        add_like("ChIJ-4qF7s5FiEgR6bRXbXOZeek", 'Bens')
        
        response = self.client.get(reverse('index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.context['likes'], 'Greggs')
        
        no_recent_eats = len(response.context['likes'])
        self.assertEqual(no_recent_eats , 4)
        
class ProfileViewTests(TestCase):
    
    def test_username_shows(self):
    
        add_user_and_profile("stevo", "stevo@gmail.com", "Greggs", "howdy")
        
        response = self.client.get(reverse('index'))
        
        self.assertEqual(response.status_code, 200)