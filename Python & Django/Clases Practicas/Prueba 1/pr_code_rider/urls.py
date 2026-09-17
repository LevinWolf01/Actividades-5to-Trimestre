from django.contrib import admin
from django.urls import path, include

from pr_code_rider import views

urlpatterns = [
    path('', views.fn_inicio),
    path('admin/', admin.site.urls),
    path('code-rider/', include ('app_code_rider.urls')),
]
