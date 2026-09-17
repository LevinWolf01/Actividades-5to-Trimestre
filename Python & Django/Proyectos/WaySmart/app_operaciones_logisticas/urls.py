from django.urls import path

from . import views

app_name = 'app_operaciones_logisticas'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('centro/nuevo/', views.crear_centro, name='crear_centro'),
    path('operador/nuevo/', views.crear_operador, name='crear_operador'),
    path('vehiculo/nuevo/', views.crear_vehiculo, name='crear_vehiculo'),
    path('envio/nuevo/', views.crear_envio, name='crear_envio'),
    path('parada/nueva/', views.crear_parada, name='crear_parada'),
    path('tipos-dato/nuevo/', views.crear_registro_tipos, name='crear_registro_tipos'),
    path('envio/<uuid:codigo>/', views.detalle_envio, name='detalle_envio'),
]