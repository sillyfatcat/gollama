from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect

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
    qs = ShortHand.objects.filter(label=shorthand)
    if not qs:
        qs = ShortHand.objects.get_similar(shorthand)
        return render(request, '404.html', status=404, context={'shorthand': shorthand, 'candidates': qs})

    obj = ShortHand.objects.get(label=shorthand)
    url = obj.url
    if not parameter and '{}' in url:
        url = url.split('{}')[0]
    elif parameter:
        if '{}' in url:
            url = url.format(parameter)
        else:
            url = f'{url.rstrip("/")}/{parameter}'
    return HttpResponseRedirect(url)
