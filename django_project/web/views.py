"""
views.py — Vistas de la app web
Archivo: web/views.py

Cada función recibe un request HTTP y devuelve
una respuesta renderizando la plantilla correspondiente.
"""

from django.shortcuts import render


def index(request):
    """
    Página principal: lista de portfolios.
    URL: /
    Template: web/templates/web/index.html
    """
    portfolios = [
        {
            'nombre': 'David Luna',
            'rol': 'Desarrollador Full Stack',
            'url': 'portfolio_david',   # nombre de la url (ver urls.py)
            'color': '#1565c0',
        },
        {
            'nombre': 'Valentina Burbano',
            'rol': 'Full Stack Developer · UI/UX Specialist',
            'url': 'portfolio_valentina',
            'color': '#4a148c',
        },
        {
            'nombre': 'Juan Sebastián Bolívar',
            'rol': 'Ingeniero de Software',
            'url': 'portfolio_sebastian',
            'color': '#1b5e20',
        },
    ]
    return render(request, 'web/index.html', {'portfolios': portfolios})


def portfolio_david(request):
    """
    Portfolio de David Luna.
    URL: /portfolio/david/
    Template: web/templates/web/portfolio_david.html
    """
    return render(request, 'web/portfolio_david.html')


def portfolio_valentina(request):
    """
    Portfolio de Valentina Burbano.
    URL: /portfolio/valentina/
    Template: web/templates/web/portfolio_valentina.html
    """
    return render(request, 'web/portfolio_valentina.html')


def portfolio_sebastian(request):
    """
    Portfolio de Juan Sebastián Bolívar.
    URL: /portfolio/sebastian/
    Template: web/templates/web/portfolio_sebastian.html
    """
    return render(request, 'web/portfolio_sebastian.html')
