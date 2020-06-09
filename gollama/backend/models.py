from datetime import date

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

    def get(self, *args, **kwargs):
        obj = super().get(*args, **kwargs)
        count_instance, _ = DailyCountInstance.objects.get_or_create(
            shorthand=obj,
            day=date.today()
        )
        count_instance.counter += 1
        count_instance.save(update_fields=['counter'])
        return obj


# Create your models here.
class ShortHand(models.Model):
    label = models.CharField(max_length=32, unique=True)
    url = models.URLField()
    objects = ShortHandManager()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'{self.label} - {self.url}'

    @property
    def stats(self):
        return {c.day: c.counter for c in DailyCountInstance.objects.filter(shorthand=self)}


class DailyCountInstance(models.Model):
    shorthand = models.ForeignKey(ShortHand, on_delete=models.CASCADE)
    day = models.DateField()
    counter = models.IntegerField(default=0)

    class Meta:
        unique_together = ('shorthand', 'day',)

    def __str__(self):
        return f'{self.shorthand}: {self.day} :{self.counter}'
