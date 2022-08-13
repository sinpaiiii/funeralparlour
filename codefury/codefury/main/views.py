from django.http import HttpResponse
from django.template import loader
from quart import template_rendered
from django.shortcuts import render



def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

