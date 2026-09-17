from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', lambda request: HttpResponse("<h1>Maracas. Bienvenido al planeta Vegita</h1>")),
    path('bienvenida', lambda request: HttpResponse("Bienvenido, <b> Mi Estimado 🟥⬜🟥Peruano🟥⬜🟥</b> ")),
    path('despedida', lambda request: HttpResponse('Gracias por ver. Dale like y Suscribete :D ')),
]