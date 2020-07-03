from django.urls import path
from . import views

urlpatterns = [
    path('page4', views.page4, name='page4'),
    path('page3', views.page3, name='page3'),
    path('page2', views.page2, name='page2'),
    path('shojo_search', views.shojo_search, name='shojo_search'),
    path('family_search', views.family_search, name='family_search'),
    path('', views.family, name='home'),
]