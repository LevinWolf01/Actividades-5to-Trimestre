from django.contrib import admin

from .models import CategoriaServicio, CentroOperativo, Envio, Etiqueta, Operador, Parada, PerfilOperador, RegistroTiposDato, Vehiculo

admin.site.register([CategoriaServicio, CentroOperativo, Envio, Etiqueta, Operador, Parada, PerfilOperador, RegistroTiposDato, Vehiculo])