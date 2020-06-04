from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponsePermanentRedirect

from backend.models import ShortHand


def index(request):
    if request.method == 'POST' and (request.POST.get('shorthand') and request.POST.get('url')):
        ShortHand.objects.create(
            label=request.POST.get('shorthand'),
            url=request.POST.get('url')
        )
        return redirect('index')

    return render(request, 'index.html', context={'shorthands': ShortHand.objects.all()})


def reroute(request, shorthand, parameter=None):
    obj = get_object_or_404(ShortHand, label=shorthand)
    url = obj.url
    print(parameter, url)
    if not parameter and '{}' in url:
        url = url.split('{}')[0]
    elif parameter:
        if '{}' in url:
            url = url.format(parameter)
        else:
            url = f'{url.rstrip("/")}/{parameter}'
    return HttpResponsePermanentRedirect(url)
