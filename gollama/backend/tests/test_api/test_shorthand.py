from django.test import TestCase
from rest_framework.test import APIClient


class TestShortHand(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_get(self):
        response_json = self.client.post('/api/v1/shorthand/', {'label': 'foo', 'url': 'http://bar.com'}).json()
        response = self.client.get(f'/api/v1/shorthand/{response_json["id"]}/')
        self.assertEqual(200, response.status_code)
        self.assertEqual({
            'id': 1,
            'label': 'foo',
            'url': 'http://bar.com'
        }, response.json())

    def test_list(self):
        self.client.post('/api/v1/shorthand/', {'label': 'foo', 'url': 'http://bar.com'})
        self.client.post('/api/v1/shorthand/', {'label': 'bar', 'url': 'http://foo.com'})
        response = self.client.get('/api/v1/shorthand/')
        self.assertEqual(200, response.status_code)
        response_json = response.json()
        self.assertEqual(2, len(response_json))

    def test_create(self):
        response = self.client.post('/api/v1/shorthand/', {'label': 'foo', 'url': 'http://bar.com'})
        self.assertEqual(201, response.status_code)
        response_json = response.json()
        self.assertEqual({
            'id': 1,
            'label': 'foo',
            'url': 'http://bar.com'
        }, response_json)

    def test_create_fail_duplicate(self):
        response = self.client.post('/api/v1/shorthand/', {'label': 'foo', 'url': 'http://bar.com'})
        self.assertEqual(201, response.status_code)
        response = self.client.post('/api/v1/shorthand/', {'label': 'foo', 'url': 'http://bar.com'})
        self.assertEqual(400, response.status_code)

    def test_update(self):
        response = self.client.post('/api/v1/shorthand/', {'label': 'foo', 'url': 'http://bar.com'})
        self.assertEqual(201, response.status_code)
        response_json = response.json()
        self.assertEqual('http://bar.com', response_json['url'])
        response = self.client.patch(f'/api/v1/shorthand/{response_json["id"]}/', {'url': 'https://bar.com'})
        self.assertEqual(200, response.status_code)
        response_json = response.json()
        self.assertEqual('https://bar.com', response_json['url'])

    def test_delete(self):
        response = self.client.post('/api/v1/shorthand/', {'label': 'foo', 'url': 'http://bar.com'})
        self.assertEqual(201, response.status_code)
        response_json = response.json()
        self.assertEqual({
            'id': 1,
            'label': 'foo',
            'url': 'http://bar.com'
        }, response_json)
        response = self.client.delete(f'/api/v1/shorthand/{response_json["id"]}/')
        self.assertEqual(204, response.status_code)
        response = self.client.get(f'/api/v1/shorthand/{response_json["id"]}/')
        self.assertEqual(404, response.status_code)
