from django.contrib import admin
from .models import Cliente, Cartelera, Pelicula, Detalle
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Cartelera)
admin.site.register(Pelicula)
admin.site.register(Detalle)