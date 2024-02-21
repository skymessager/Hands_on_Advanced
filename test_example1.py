import numpy as np

def fahrenheit2celcius(T_f):
    """
    Convert temperature in Fahrenheit to Celcius
    """
    T_c = (T_f - 32.) * (5/9.)
    return T_c


def test_fahrenheit2celcius():
    T_c = fahrenheit2celcius(32.)
    expected_result = 0.
    assert T_c == expected_result

