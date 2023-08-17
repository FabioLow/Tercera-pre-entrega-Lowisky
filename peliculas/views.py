from django.shortcuts import render, redirect
from .forms import PeliculaForm, DirectorForm, GeneroForm, BusquedaForm
from .models import Pelicula

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_pelicula')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/agregar_pelicula.html', {'form': form})

def agregar_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_director')
    else:
        form = DirectorForm()
    return render(request, 'peliculas/agregar_director.html', {'form': form})

def agregar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_genero')
    else:
        form = GeneroForm()
    return render(request, 'peliculas/agregar_genero.html', {'form': form})

def buscar(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Pelicula.objects.filter(titulo__icontains=termino_busqueda)
    else:
        form = BusquedaForm()
    return render(request, 'peliculas/buscar.html', {'form': form, 'resultados': resultados})

def inicio(request):
    return render(request, 'peliculas/inicio.html')
