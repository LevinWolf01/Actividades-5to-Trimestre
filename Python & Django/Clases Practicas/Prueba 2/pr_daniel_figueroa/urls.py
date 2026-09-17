from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dani-figue/', include ('app_daniel_figueroa.urls')),
]
