from django.urls import path
from . import views

urlpatterns = [
    path('temblor/', views.ingreso_temblor, name='ingreso_temblor'),
    path('temblor-salida/', views.salida_temblor, name='salida_temblor'),
]