from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def greetings(request):
    template = loader.get_template('about/index.html')
    return HttpResponse(template.render())

def aboutMe(request):
    template = loader.get_template('about/about.html')
    return HttpResponse(template.render())

def contactMe(request):
    return render(request, 'about/contact.html')