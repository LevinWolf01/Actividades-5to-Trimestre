import uuid

from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models


class CategoriaServicio(models.Model):
    codigo = models.SlugField(max_length=40, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=100, verbose_name='Nombre de categoría')
    descripcion = models.TextField(blank=True, help_text='Describe el tipo de servicio.')
    activa = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Categoría de servicio'
        verbose_name_plural = 'Categorías de servicio'

    def __str__(self):
        return self.nombre


class CentroOperativo(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True, db_column='codigo_centro')
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=80, db_index=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    configuracion = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['ciudad', 'nombre']
        verbose_name = 'Centro operativo'
        verbose_name_plural = 'Centros operativos'

    def __str__(self):
        return f'{self.codigo} · {self.nombre}'


class Operador(models.Model):
    documento = models.PositiveBigIntegerField(unique=True)
    nombre = models.CharField(max_length=120)
    correo = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    foto = models.ImageField(upload_to='operadores/', blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class PerfilOperador(models.Model):
    operador = models.OneToOneField(Operador, on_delete=models.CASCADE, related_name='perfil')
    zona_preferida = models.CharField(max_length=80)
    calificacion = models.FloatField(default=5.0, validators=[MinValueValidator(0)])
    biografia = models.TextField(blank=True)

    def __str__(self):
        return f'Perfil de {self.operador}'


class Vehiculo(models.Model):
    TIPOS = [('moto', 'Motocicleta'), ('van', 'Van'), ('camion', 'Camión')]

    placa = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPOS, default='moto')
    capacidad_kg = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    disponible = models.BooleanField(default=True)
    ficha_tecnica = models.FilePathField(path=settings.BASE_DIR, match=r'.*\\.(pdf|txt)$', blank=True)

    class Meta:
        ordering = ['placa']

    def __str__(self):
        return f'{self.placa} · {self.get_tipo_display()}'


class Envio(models.Model):
    ESTADOS = [
        ('programado', 'Programado'),
        ('en_ruta', 'En ruta'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Código de envío')
    categoria = models.ForeignKey(
        CategoriaServicio,
        on_delete=models.PROTECT,
        related_name='envios',
        related_query_name='envio',
        limit_choices_to={'activa': True},
    )
    centro = models.ForeignKey(
        CentroOperativo,
        on_delete=models.PROTECT,
        to_field='codigo',
        db_column='centro_codigo',
        related_name='envios',
    )
    operador = models.ForeignKey(
        Operador, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='envios',
    )
    vehiculo = models.ForeignKey(
        Vehiculo, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='envios',
    )
    etiquetas = models.ManyToManyField('Etiqueta', blank=True, related_name='envios')
    referencia = models.CharField(max_length=50, unique=True, db_index=True)
    descripcion = models.TextField(help_text='Contenido y observaciones del paquete.')
    estado = models.CharField(max_length=12, choices=ESTADOS, default='programado')
    peso_kg = models.FloatField(validators=[MinValueValidator(0.01)])
    cantidad = models.PositiveIntegerField(default=1)
    prioridad = models.SmallIntegerField(default=2, validators=[MinValueValidator(1)])
    hora_recoleccion = models.TimeField(null=True, blank=True)
    seguimiento_url = models.URLField(max_length=300, blank=True)
    comprobante = models.ImageField(upload_to='comprobantes/', blank=True)
    datos_extra = models.JSONField(default=dict, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado_en = models.DateTimeField(auto_now=True, db_comment='Última modificación del envío')

    class Meta:
        ordering = ['-creado_en']
        db_table = 'operaciones_envio'

    def __str__(self):
        return self.referencia


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=7, default='#0d766f', help_text='Color hexadecimal, por ejemplo #0d766f.')

    def __str__(self):
        return self.nombre


class Parada(models.Model):
    ESTADOS = [('pendiente', 'Pendiente'), ('visitada', 'Visitada'), ('fallida', 'Fallida')]

    envio = models.ForeignKey(Envio, on_delete=models.CASCADE, related_name='paradas')
    secuencia = models.PositiveSmallIntegerField()
    destinatario = models.CharField(max_length=150)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=30, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['envio', 'secuencia']
        constraints = [models.UniqueConstraint(fields=['envio', 'secuencia'], name='parada_unica_por_envio')]

    def __str__(self):
        return f'{self.envio} · parada {self.secuencia}'


class RegistroTiposDato(models.Model):
    """Formulario práctico que reúne los tipos y opciones de las tablas de referencia."""

    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ruta_archivo = models.FilePathField(path=settings.BASE_DIR, blank=True)
    decimal = models.FloatField(default=0.0)
    direccion_ip = models.GenericIPAddressField(null=True, blank=True)
    imagen = models.ImageField(upload_to='registros/', blank=True)
    entero = models.IntegerField(default=0)
    datos_json = models.JSONField(default=dict, blank=True)
    entero_grande_positivo = models.PositiveBigIntegerField(default=0)
    entero_positivo = models.PositiveIntegerField(default=0)
    entero_pequeno_positivo = models.PositiveSmallIntegerField(default=0)
    slug = models.SlugField(max_length=100, blank=True)
    entero_pequeno = models.SmallIntegerField(default=0)
    texto = models.TextField(blank=True)
    hora = models.TimeField(null=True, blank=True)
    url = models.URLField(max_length=300, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Registro de tipos de dato'
        verbose_name_plural = 'Registros de tipos de dato'