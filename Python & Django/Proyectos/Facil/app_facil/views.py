from django.shortcuts import render
from .models import Temblor


def ingreso_temblor(request):
    ultimo_temblor = None

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'enviar':
            nuevo_temblor = Temblor.objects.create(
                magnitud=request.POST.get('magnitud'),
                profundidad=request.POST.get('profundidad'),
                rango=request.POST.get('rango'),
                lugar=request.POST.get('lugar'),
                area=request.POST.get('area'),
                fecha=request.POST.get('fecha'),
                hora=request.POST.get('hora'),
                observaciones=request.POST.get('observaciones')
            )
            ultimo_temblor = nuevo_temblor
            return render(request, 'temblor.html', {'ultimo_temblor': ultimo_temblor})

        if accion == 'listar':
            registros = Temblor.objects.all().order_by('-fecha', '-hora', '-id')
            return render(request, 'salida-temblor.html', {'temblores': registros})

        if accion == 'buscar':
            campo = request.POST.get('filtro')
            criterio = request.POST.get('criterio_busqueda')
            registros = []

            if campo and criterio:
                filtros = {
                    'magnitud': 'magnitud',
                    'profundidad': 'profundidad',
                    'lugar': 'lugar__icontains',
                    'area': 'area__icontains',
                    'rango': 'rango__icontains',
                    'fecha': 'fecha',
                    'hora': 'hora',
                }

                field_name = filtros.get(campo)
                if field_name in ('magnitud', 'profundidad'):
                    try:
                        valor = float(criterio)
                        registros = list(Temblor.objects.filter(**{field_name: valor}).order_by('-id'))
                    except ValueError:
                        registros = []
                elif field_name in ('fecha', 'hora'):
                    if campo == 'fecha':
                        registros = list(Temblor.objects.filter(fecha=criterio).order_by('-id'))
                    else:
                        registros = list(Temblor.objects.filter(hora=criterio).order_by('-id'))
                else:
                    registros = list(Temblor.objects.filter(**{field_name: criterio}).order_by('-id'))

            return render(request, 'salida-temblor.html', {'temblores': registros})

    return render(request, 'temblor.html', {'ultimo_temblor': ultimo_temblor})


def salida_temblor(request):
    registros = Temblor.objects.all().order_by('-fecha', '-hora', '-id')
    return render(request, 'salida-temblor.html', {'temblores': registros})