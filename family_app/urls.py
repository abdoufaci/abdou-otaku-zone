from django.urls import path
from . import views

urlpatterns = [
    path('blue_page4', views.blue_page4, name='blue_page4'),
    path('blue_page3', views.blue_page3, name='blue_page3'),
    path('blue_page2', views.blue_page2, name='blue_page2'),
    path('blue_search', views.blue_search, name='blue_search'),
    path('blue', views.blue, name='blue'),
    path('green_page4', views.green_page4, name='green_page4'),
    path('green_page3', views.green_page3, name='green_page3'),
    path('green_page2', views.green_page2, name='green_page2'),
    path('green_search', views.green_search, name='green_search'),
    path('green', views.green, name='green'),
    path('red_page4', views.red_page4, name='red_page4'),
    path('red_page3', views.red_page3, name='red_page3'),
    path('red_page2', views.red_page2, name='red_page2'),
    path('red_search', views.red_search, name='red_search'),
    path('red', views.red, name='red'),
    path('page4', views.page4, name='page4'),
    path('page3', views.page3, name='page3'),
    path('page2', views.page2, name='page2'),
    path('shojo_search', views.shojo_search, name='shojo_search'),
    path('family_search', views.family_search, name='family_search'),
    path('', views.family, name='home'),
]