from django.http import HttpResponse
from django.template import loader
from quart import template_rendered
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')