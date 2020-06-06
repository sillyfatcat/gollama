from django.db import models
from textdistance import levenshtein


def levenshtein_ratio(s, t):
    return 1 - (levenshtein(s, t) / ((len(s) + len(t)) / 2))


class ShortHandManager(models.Manager):
    def get_similar(self, label):
        candidates = [(c, levenshtein_ratio(label, c.label)) for c in self.all()]
        candidates.sort(key=lambda x: x[1], reverse=True)
        candidates = [candidate[0].id for candidate in candidates if candidate[1] > .5]
        return self.filter(id__in=candidates)


# Create your models here.
class ShortHand(models.Model):
    label = models.CharField(max_length=32, unique=True)
    url = models.URLField()
    objects = ShortHandManager()

    def __str__(self):
        return f'{self.label} - {self.url}'
