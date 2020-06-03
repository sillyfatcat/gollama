from django.test import Client
from django.test import TestCase

from backend.models import ShortHand


class TestCreate(TestCase):
    def setUp(self):
        self.client = Client()

    def test_creating_shorthand_from_url(self):
        self.assertFalse(ShortHand.objects.filter(url='http://bar.com', label='foo').exists())
        response = self.client.post('/', {'shorthand': 'foo', 'url': 'http://bar.com'})
        self.assertTrue(ShortHand.objects.filter(url='http://bar.com', label='foo').exists())

