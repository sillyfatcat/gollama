from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponsePermanentRedirect

from backend.models import ShortHand


def index(request):
    print(request.POST)
    if request.method == 'POST' and (request.POST.get('shorthand') and request.POST.get('url')):
        ShortHand.objects.create(
            label=request.POST.get('shorthand'),
            url=request.POST.get('url')
        )
        return redirect('index')

    return render(request, 'index.html', context={'shorthands': ShortHand.objects.all()})


def reroute(request, shorthand):
    obj = get_object_or_404(ShortHand, label=shorthand)
    return HttpResponsePermanentRedirect(obj.url)
