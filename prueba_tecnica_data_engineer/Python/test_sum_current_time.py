# Archivo test_sum_current_time.py: Pruebas unitarias para la función de suma de tiempo.

import pytest
from logica import sum_current_time

def test_sum_current_time():
    assert sum_current_time("01:02:03") == 6
    assert sum_current_time("12:34:56") == 21
    assert sum_current_time("00:00:00") == 0
    assert sum_current_time("10:59:02") == 17
