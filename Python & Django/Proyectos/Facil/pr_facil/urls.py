from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from pr_facil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fn_inicio),
    path('', RedirectView.as_view(url='', permanent=False)),
    
    path('popayan/', views.fn_popayan),
    path('popayan/', include('app_facil.urls')),
]
