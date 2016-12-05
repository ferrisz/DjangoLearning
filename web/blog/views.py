from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from blog.models import Host

# Create your views here.

def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))

def db(req):
    n1 = Host(hostname = 'node2', ip = '2.2.2.2')
    n1.save()
    return HttpResponse('OK')