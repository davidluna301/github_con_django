#!/usr/bin/env python
"""
manage.py — Utilidad de línea de comandos de Django
Archivo: manage.py (raíz del proyecto)

Uso:
  python manage.py runserver        → inicia el servidor de desarrollo
  python manage.py migrate          → aplica migraciones
  python manage.py collectstatic    → reúne estáticos para producción
"""

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolios_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y activado el entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
