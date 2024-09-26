# Archivo logica.py: Soluciones de lógica para la prueba técnica.

from datetime import datetime, timedelta

# Ejercicio 1: Función para calcular el inicio de la semana.
def week_start_date(date: str, on_monday: bool = True) -> str:
    date_obj = datetime.strptime(date, "%d/%m/%Y")
    weekday = date_obj.weekday()
    if on_monday:
        start_of_week = date_obj - timedelta(days=weekday)
    else:
        start_of_week = date_obj - timedelta(days=(weekday + 1) % 7)
    return start_of_week.strftime("%d/%m/%Y")
