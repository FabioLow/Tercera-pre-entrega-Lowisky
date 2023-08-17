from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField()
    precio_alquiler = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.titulo
    
class Director(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre