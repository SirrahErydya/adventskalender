from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models


# Create your views here.
def index(request):
    windows = models.Window.objects.order_by('day')
    config = models.Config.load()
    template = loader.get_template('index.html')
    context = {
        'windows': windows,
        'config': config
    }
    return HttpResponse(template.render(context, request))
