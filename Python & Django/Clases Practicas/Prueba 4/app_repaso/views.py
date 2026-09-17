from django.shortcuts import render, redirect
from .models import Mi_curso
from django.http import HttpResponse

def bienvenidoAPP(request):
    return render(request, 'app_repaso/bienvenidoAPP.html')

def crear_curso(request):
    mis_cusrsos_disponibles = [
        
        Mi_curso(
            titulo_capacitacion='Capacitacion en Python',
            duracion='3 meses',
            tipo='Online',
            detalle='Aprende Python.',
            
            instructor='Alexander Salazar',
            competencia='Algoritmia',
            ambiente='Laboratorio ADSO 1',
            aprendiz='Daniel Figueroa',
            
        ),
        
        
        Mi_curso(
            titulo_capacitacion='Capacitacion en Django',
            duracion='2 meses',
            tipo='Presencial',
            detalle='Desarrolla aplicaciones con Django.',
            
            instructor='Rider Benavides',
            competencia='Algoritmia',
            ambiente='Laboratorio ADSO 1',
            aprendiz='Deivi Perez',
        ),

        
        Mi_curso(
            titulo_capacitacion='Capacitacion con Data Science',
            duracion='4 meses',
            tipo='Online',
            detalle='Explora el mundo de análisis de datos y la ciencia de datos.',
            
            instructor='Edwin Velazco',
            competencia='Bases de Datos RELACIONALES',
            ambiente='Laboratorio ADSO 3',
            aprendiz='Juliana Velazco',
        ),
        
    
        Mi_curso(
            titulo_capacitacion='Capacitacion con Data Science',
            duracion='4 meses',
            tipo='Online',
            detalle='Explora el mundo de análisis de datos y la ciencia de datos.',
            
            instructor='Cesar Cuellar',
            competencia='Bases de Datos  NO RELACIONALES',
            ambiente='Laboratorio ADSO 1',
            aprendiz='Miguel Angel',
        ),
    ]

    Mi_curso.objects.bulk_create(mis_cusrsos_disponibles)
    return HttpResponse('Convocatorias creadas correctamente! ✅')

def listar_Cursos(request):
    mis_cusrsos_disponibles = Mi_curso.objects.all()
    return render(
        request,
        "app_repaso/crear_curso.html",
        {'mis_cusrsos_disponibles': mis_cusrsos_disponibles},
    )




