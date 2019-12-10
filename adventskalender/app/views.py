from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from . import models
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def login_redirect(request):
    return redirect('login')


@login_required
def index(request):
    windows = models.Window.objects.order_by('day')
    config = models.Config.load()
    template = loader.get_template('index.html')
    context = {
        'windows': windows,
        'config': config
    }
    return HttpResponse(template.render(context, request))


@login_required
def open_window(request):
    day = json.loads(request.body)['day']
    window = models.Window.objects.get(day=day)
    window.open = True
    window.save()
    return redirect('index')


@login_required
def load_image(request):
    day = json.loads(request.body)['day']
    window = models.Window.objects.get(day=day)
    return JsonResponse({ 'url': window.content.url, 'descr': window.description})