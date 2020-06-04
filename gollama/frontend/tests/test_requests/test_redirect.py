from django.test import Client
from django.test import TestCase

from backend.models import ShortHand


class TestRedirect(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_shorthand_that_doesnt_exist(self):
        response = self.client.get('/foo')
        self.assertEqual(404, response.status_code)

    def test_requesting_shorthand_exists(self):
        ShortHand.objects.create(label='foo', url='https://google.com')
        response = self.client.get('/foo', follow=True)
        self.assertEqual(('https://google.com', 301), response.redirect_chain[0])

    def test_requesting_shorthand_with_wildcard_params(self):
        """
        go/foo/123 -> foo.com/search?q=123
        :return:
        """
        ShortHand.objects.create(label='foo', url='https://www.google.com/search?q={}')
        response = self.client.get('/foo/123', follow=True)
        self.assertEqual(('https://www.google.com/search?q=123', 301), response.redirect_chain[0])

    def test_requesting_shorthand_with_wildcard_params_but_no_param(self):
        ShortHand.objects.create(label='foo', url='https://www.google.com/search?q={}')
        response = self.client.get('/foo', follow=True)
        self.assertEqual(('https://www.google.com/search?q=', 301), response.redirect_chain[0])

    def test_trailing_parameter(self):
        ShortHand.objects.create(label='foo', url='https://twitch.tv')
        response = self.client.get('/foo/bar', follow=True)
        self.assertEqual(('https://twitch.tv/bar', 301), response.redirect_chain[0])

    def test_trailing_parameter_with_trailing_slash(self):
        ShortHand.objects.create(label='foo', url='https://twitch.tv/')
        response = self.client.get('/foo/bar', follow=True)
        self.assertEqual(('https://twitch.tv/bar', 301), response.redirect_chain[0])
