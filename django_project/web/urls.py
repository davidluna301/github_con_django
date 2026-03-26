"""
urls.py — Rutas de la app web
Archivo: web/urls.py

Mapa de URLs:
  /                        → index (lista de portfolios)
  /portfolio/david/        → portfolio de David
  /portfolio/valentina/    → portfolio de Valentina
  /portfolio/sebastian/    → portfolio de Sebastián
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/david/',     views.portfolio_david,     name='portfolio_david'),
    path('portfolio/valentina/', views.portfolio_valentina, name='portfolio_valentina'),
    path('portfolio/sebastian/', views.portfolio_sebastian, name='portfolio_sebastian'),
]
