from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from .import views
from pr_repaso import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fn_inicio),
    path('', include('app_repaso.urls')),
]
