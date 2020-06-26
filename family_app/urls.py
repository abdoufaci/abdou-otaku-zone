from django.urls import path
from . import views

urlpatterns = [
    path('shojo_search', views.shojo_search, name='shojo_search'),
    path('family_search', views.family_search, name='family_search'),
    path('', views.family, name='home'),
]