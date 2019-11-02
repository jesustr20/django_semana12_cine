from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellido = models.CharField(max_length=200, blank=False, null=False)
    dni = models.CharField(max_length=10, blank=False, null=False)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}'

class Cartelera(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    genero = models.CharField(max_length=200, blank=False, null=False)
    Nro_de_sala = models.CharField(max_length=10, blank=False, null=False)
    duracion = models.CharField(max_length=8, blank=False, null=False)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return f'Pelicula: {self.title} - Genero: {self.genero} - {self.Nro_de_sala} - Duracion: {self.duracion}'

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    cartelera = models.ForeignKey('Cartelera', on_delete=models.CASCADE, null=True)
    entradas = models.IntegerField(default=1)
    horario = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return f'{self.cartelera} | Nro. Entradas: {self.entradas} - Horario: {self.horario}'

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True)
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.cliente} - {self.pelicula}'