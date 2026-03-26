"""
urls.py — URLs raíz del proyecto
Archivo: portfolios_project/urls.py
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Todas las rutas de la app 'web' arrancan desde la raíz
    path('', include('web.urls')),
]
