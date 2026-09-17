from django import forms

from .models import (
    CategoriaServicio,
    CentroOperativo,
    Envio,
    Operador,
    Parada,
    RegistroTiposDato,
    Vehiculo,
)


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'field-control')


class CategoriaServicioForm(StyledModelForm):
    class Meta:
        model = CategoriaServicio
        fields = '__all__'


class CentroOperativoForm(StyledModelForm):
    class Meta:
        model = CentroOperativo
        fields = '__all__'


class OperadorForm(StyledModelForm):
    class Meta:
        model = Operador
        fields = '__all__'


class VehiculoForm(StyledModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class EnvioForm(StyledModelForm):
    class Meta:
        model = Envio
        exclude = ['codigo', 'creado_en', 'actualizado_en']
        widgets = {
            'hora_recoleccion': forms.TimeInput(attrs={'type': 'time'}),
            'datos_extra': forms.Textarea(attrs={'rows': 3}),
        }


class ParadaForm(StyledModelForm):
    class Meta:
        model = Parada
        fields = '__all__'


class RegistroTiposDatoForm(StyledModelForm):
    class Meta:
        model = RegistroTiposDato
        exclude = ['codigo', 'creado', 'actualizado']
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'datos_json': forms.Textarea(attrs={'rows': 3}),
        }