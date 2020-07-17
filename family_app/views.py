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





def page2(request):
    return render(request, 'my_app/page2.html',)


def page3(request):
    return render(request, 'my_app/page3.html',)


def page4(request):
    return render(request, 'my_app/page4.html',)


def movie(request):
    return render(request, 'my_app/movie.html',)


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


def red_movie(request):
    return render(request, 'red/red_movie.html',)


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


def green_movie(request):
    return render(request, 'green/green_movie.html',)


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


def blue_movie(request):
    return render(request, 'blue/blue_movie.html',)


def pink(request):
    return render(request, 'pink/base5.html',)


def pink_search(request):
    request.method
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request, 'pink/search5.html', stuff_for_frontend)


def pink_page2(request):
    return render(request, 'pink/pink_page2.html',)


def pink_page3(request):
    return render(request, 'pink/pink_page3.html',)


def pink_page4(request):
    return render(request, 'pink/pink_page4.html',)


def pink_movie(request):
    return render(request, 'pink/pink_movie.html',)


def purple(request):
    return render(request, 'purple/base6.html',)


def purple_search(request):
    request.method
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request, 'purple/search6.html', stuff_for_frontend)


def purple_page2(request):
    return render(request, 'purple/purple_page2.html',)


def purple_page3(request):
    return render(request, 'purple/purple_page3.html',)


def purple_page4(request):
    return render(request, 'purple/purple_page4.html',)


def purple_movie(request):
    return render(request, 'purple/purple_movie.html',)


def white(request):
    return render(request, 'white/base8.html',)


def white_search(request):
    request.method
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request, 'white/search8.html', stuff_for_frontend)


def white_page2(request):
    return render(request, 'white/white_page2.html',)


def white_page3(request):
    return render(request, 'white/white_page3.html',)


def white_page4(request):
    return render(request, 'white/white_page4.html',)


def white_movie(request):
    return render(request, 'white/white_movie.html',)