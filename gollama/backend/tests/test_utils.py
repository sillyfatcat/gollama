from django.test import TestCase

from backend.models import levenshtein_ratio


class TestLevenshteinRatio(TestCase):
    def test_distance_same_str(self):
        self.assertEqual(1, levenshtein_ratio('foo', 'foo'))

    def test_distance_similar_str(self):
        self.assertEqual(.6, levenshtein_ratio('foo', 'fo'))

    def test_distance_very_different_str(self):
        self.assertEqual(0, levenshtein_ratio('foo', 'bar'))
