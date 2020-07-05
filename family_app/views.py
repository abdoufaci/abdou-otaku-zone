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


def red(request):
    return render(request, 'base2.html',)


def red_search(request):
    request.method
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request, 'my_app/search2.html', stuff_for_frontend)


def red_page2(request):
    return render(request, 'red/red_page2.html',)


def red_page3(request):
    return render(request, 'red/red_page3.html',)


def red_page4(request):
    return render(request, 'red/red_page4.html',)


def green(request):
    return render(request, 'green/base3.html',)


def green_search(request):
    request.method
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request, 'green/search3.html', stuff_for_frontend)


def green_page2(request):
    return render(request, 'green/green_page2.html',)


def green_page3(request):
    return render(request, 'green/green_page3.html',)


def green_page4(request):
    return render(request, 'green/green_page4.html',)


def blue(request):
    return render(request, 'blue/base4.html',)


def blue_search(request):
    request.method
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request, 'blue/search4.html', stuff_for_frontend)


def blue_page2(request):
    return render(request, 'blue/blue_page2.html',)


def blue_page3(request):
    return render(request, 'blue/blue_page3.html',)


def blue_page4(request):
    return render(request, 'blue/blue_page4.html',)