from django.db.utils import IntegrityError
from django.test import TestCase

from backend.serializers import ShortHandSerializer


class TestShortHand(TestCase):
    def test_validate_true(self):
        serialized = ShortHandSerializer(data={'label': 'foo', 'url': 'http://foo.com'})
        self.assertTrue(serialized.is_valid())

    def test_validate_false(self):
        serialized = ShortHandSerializer(data={'url': 'http://foo.com'})
        self.assertFalse(serialized.is_valid())
        serialized = ShortHandSerializer(data={'label': 'foo'})
        self.assertFalse(serialized.is_valid())

    def test_create(self):
        serialized = ShortHandSerializer(data={'label': 'foo', 'url': 'http://foo.com'})
        serialized.is_valid()
        obj = serialized.save()
        self.assertIsNotNone(obj)
        self.assertEqual(1, obj.id)
        self.assertEqual('foo', obj.label)
        self.assertEqual('http://foo.com', obj.url)

    def test_create_fail_duplicate(self):
        serialized = ShortHandSerializer(data={'label': 'foo', 'url': 'http://foo.com'})
        serialized.is_valid()
        obj = serialized.save()
        self.assertIsNotNone(obj)
        serialized = ShortHandSerializer(data={'label': 'foo', 'url': 'http://foo.com'})
        self.assertFalse(serialized.is_valid())

    def test_update(self):
        serialized = ShortHandSerializer(data={'label': 'foo', 'url': 'http://foo.com'})
        serialized.is_valid()
        obj = serialized.save()
        serialized = ShortHandSerializer(obj, {'url': 'http://bar.com'}, partial=True)
        self.assertTrue(serialized.is_valid())
        obj = serialized.save()
        self.assertEqual('http://bar.com', obj.url)

    def test_json(self):
        serialized = ShortHandSerializer(data={'label': 'foo', 'url': 'http://foo.com'})
        serialized.is_valid()
        obj = serialized.save()
        self.assertEqual({
            'id': 1,
            'label': 'foo',
            'url': 'http://foo.com',
        }, ShortHandSerializer(obj).data)
