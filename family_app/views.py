import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models



def family(request):
    return render(request, 'basefamily.html')


def family_search(request):
    request.method
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request, 'my_app/family_search.html', stuff_for_frontend)

def shojo_search(request):


    return render(request, 'my_app/shojo_search.html',)


def page2(request):


    return render(request, 'my_app/page2.html',)


def page3(request):


    return render(request, 'my_app/page3.html',)


def page4(request):


    return render(request, 'my_app/page4.html',)