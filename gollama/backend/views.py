from rest_framework import viewsets

from .models import ShortHand
from .serializers import ShortHandSerializer


class ShortHandViewSet(viewsets.ModelViewSet):
    queryset = ShortHand.objects.all()
    serializer_class = ShortHandSerializer
