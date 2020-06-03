from django.test import Client
from django.test import TestCase

from backend.models import ShortHand


class TestCreate(TestCase):
    def setUp(self):
        self.client = Client()

    def test_creating_shorthand_from_url(self):
        self.fail('todo')

