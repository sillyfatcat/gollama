from django.db.utils import IntegrityError
from django.test import TestCase

from backend.models import ShortHand


class TestShortHand(TestCase):
    def test_creating_short_hand(self):
        s = ShortHand.objects.create(
            label='foo',
            url='https://foo.com'
        )
        self.assertIsNotNone(s)

    def test_unique_constraint(self):
        ShortHand.objects.create(
            label='foo',
            url='https://foo.com'
        )
        with self.assertRaises(IntegrityError):
            ShortHand.objects.create(
                label='foo',
                url='https://bar.com'
            )

    def test_str_representation(self):
        s = ShortHand.objects.create(
            label='foo',
            url='https://foo.com'
        )
        self.assertEqual('foo - https://foo.com', str(s))