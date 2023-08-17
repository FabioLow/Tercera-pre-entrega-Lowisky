from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('agregar_director/', views.agregar_director, name='agregar_director'),
    path('agregar_genero/', views.agregar_genero, name='agregar_genero'),
    path('buscar/', views.buscar, name='buscar'),
]