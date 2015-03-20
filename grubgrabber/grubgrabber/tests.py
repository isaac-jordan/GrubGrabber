from django.test import TestCase
from django.core.urlresolvers import reverse

class IndexViewTests(TestCase):
    def test_index_view_with_no_recent_eats(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recent eats")