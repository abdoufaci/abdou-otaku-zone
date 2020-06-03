from django.urls import path
from . import views

urlpatterns = [
    path('family_search', views.family_search, name='family_search'),
    path('', views.family, name='home'),
]