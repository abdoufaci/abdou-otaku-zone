import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


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
