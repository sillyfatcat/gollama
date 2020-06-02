from django.db import models


# Create your models here.
class ShortHand(models.Model):
    label = models.CharField(max_length=32, unique=True)
    url = models.URLField()

    def __str__(self):
        return f'{self.label} - {self.url}'
