from rest_framework import serializers

from .models import ShortHand


class ShortHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortHand
        fields = ['id', 'label', 'url',]