from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .import views
from app_repaso import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('miRepaso/', views.bienvenidoAPP),
    path('crear-curso/', views.crear_curso),
    path('listar-cursos/', views.listar_Cursos, name='listar_cursos'),
]