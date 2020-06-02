from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponsePermanentRedirect

from backend.models import ShortHand


def index(request):
    render(request, 'index.html')


def redirect(request, shorthand):
    obj = get_object_or_404(ShortHand, label=shorthand)
    return HttpResponsePermanentRedirect(obj.url)
