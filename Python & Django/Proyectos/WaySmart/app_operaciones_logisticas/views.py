from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    CategoriaServicioForm,
    CentroOperativoForm,
    EnvioForm,
    OperadorForm,
    ParadaForm,
    RegistroTiposDatoForm,
    VehiculoForm,
)
from .models import CategoriaServicio, CentroOperativo, Envio, Operador, Parada, RegistroTiposDato, Vehiculo


def dashboard(request):
    context = {
        'envios': Envio.objects.select_related('categoria', 'centro', 'operador').all()[:8],
        'total_envios': Envio.objects.count(),
        'total_paradas': Parada.objects.count(),
        'total_centros': CentroOperativo.objects.count(),
        'total_vehiculos': Vehiculo.objects.count(),
        'categorias': CategoriaServicio.objects.filter(activa=True),
    }
    return render(request, 'app_operaciones_logisticas/dashboard.html', context)


def crear_entidad(request, form_class, titulo, template='app_operaciones_logisticas/formulario.html'):
    form = form_class(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'{titulo} guardado correctamente.')
        return redirect('app_operaciones_logisticas:dashboard')
    return render(request, template, {'form': form, 'titulo': titulo})


def crear_categoria(request):
    return crear_entidad(request, CategoriaServicioForm, 'Categoría')


def crear_centro(request):
    return crear_entidad(request, CentroOperativoForm, 'Centro operativo')


def crear_operador(request):
    return crear_entidad(request, OperadorForm, 'Operador')


def crear_vehiculo(request):
    return crear_entidad(request, VehiculoForm, 'Vehículo')


def crear_envio(request):
    return crear_entidad(request, EnvioForm, 'Envío')


def crear_parada(request):
    return crear_entidad(request, ParadaForm, 'Parada')


def crear_registro_tipos(request):
    return crear_entidad(request, RegistroTiposDatoForm, 'Registro de tipos de dato', 'app_operaciones_logisticas/tipos_dato.html')


def detalle_envio(request, codigo):
    envio = get_object_or_404(Envio.objects.select_related('categoria', 'centro', 'operador', 'vehiculo'), codigo=codigo)
    return render(request, 'app_operaciones_logisticas/detalle_envio.html', {'envio': envio})