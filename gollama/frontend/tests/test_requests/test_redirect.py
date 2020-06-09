from django.test import Client
from django.test import TestCase
from freezegun import freeze_time
from freezegun.api import FakeDate

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
        ShortHand.objects.create(label='foo', url='https://www.google.com/search?q={}&foobar')
        response = self.client.get('/foo/123', follow=True)
        self.assertEqual(('https://www.google.com/search?q=123&foobar', 301), response.redirect_chain[0])

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

    @freeze_time('2020/01/01')
    def test_counter_increases_single_day(self):
        s_1 = ShortHand.objects.create(label='foo', url='https://google.com')
        s_2 = ShortHand.objects.create(label='bar', url='https://google.com')
        self.assertEqual({}, s_1.stats)
        self.client.get('/foo', follow=True)
        self.assertEqual({FakeDate(2020, 1, 1): 1}, s_1.stats)
        self.client.get('/foo', follow=True)
        self.assertEqual({FakeDate(2020, 1, 1): 2}, s_1.stats)
        self.assertEqual({}, s_2.stats)

    def test_counter_increased_several_days(self):
        s = ShortHand.objects.create(label='foo', url='https://google.com')
        self.assertEqual({}, s.stats)
        with freeze_time('2020/01/01'):
            self.client.get('/foo', follow=True)
            self.assertEqual({FakeDate(2020, 1, 1): 1}, s.stats)
        with freeze_time('2020/01/02'):
            self.client.get('/foo', follow=True)
            self.client.get('/foo', follow=True)
            self.assertEqual({
                FakeDate(2020, 1, 1): 1,
                FakeDate(2020, 1, 2): 2
            }, s.stats)
