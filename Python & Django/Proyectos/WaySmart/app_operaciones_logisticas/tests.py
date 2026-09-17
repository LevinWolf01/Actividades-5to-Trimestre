from django.test import TestCase

from app_operaciones_logisticas.models import CategoriaServicio, CentroOperativo, Envio, Etiqueta, Operador, PerfilOperador


class OperacionesLogisticasTests(TestCase):
    def test_envio_conserva_relaciones(self):
        categoria = CategoriaServicio.objects.create(codigo='express', nombre='Express')
        centro = CentroOperativo.objects.create(codigo='BOG-01', nombre='Centro Bogotá', direccion='Calle 1', ciudad='Bogotá')
        envio = Envio.objects.create(
            categoria=categoria, centro=centro, referencia='WS-001', descripcion='Paquete de prueba', peso_kg=1.5,
        )
        self.assertEqual(envio.categoria.nombre, 'Express')
        self.assertEqual(envio.centro.codigo, 'BOG-01')

    def test_relaciones_uno_a_uno_y_muchos_a_muchos(self):
        operador = Operador.objects.create(documento=123456, nombre='Ana Ruiz', correo='ana@example.com')
        PerfilOperador.objects.create(operador=operador, zona_preferida='Norte')
        etiqueta = Etiqueta.objects.create(nombre='Frágil')
        categoria = CategoriaServicio.objects.create(codigo='standard', nombre='Standard')
        centro = CentroOperativo.objects.create(codigo='MED-01', nombre='Centro Medellín', direccion='Calle 2', ciudad='Medellín')
        envio = Envio.objects.create(categoria=categoria, centro=centro, operador=operador, referencia='WS-002', descripcion='Caja', peso_kg=2)
        envio.etiquetas.add(etiqueta)
        self.assertEqual(operador.perfil.zona_preferida, 'Norte')
        self.assertEqual(envio.etiquetas.first(), etiqueta)