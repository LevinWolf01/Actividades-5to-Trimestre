from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pr_waysmart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waysmart/', views.fn_inicio),
    # Las rutas del app quedan disponibles bajo /waysmart/.
    path('waysmart/', include('app_destinos_servicios.urls')),
    path('catalogo/', include('app_operaciones_logisticas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
