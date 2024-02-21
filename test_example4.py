# contents of test_example4.py
import pytest
import numpy.testing as npt
import numpy as np

def fahrenheit2celcius(T_f):
    """
    Convert temperature in Fahrenheit to Celcius
    """
    if not np.isreal(T_f):
        raise TypeError("Temperature needs to be a real value")
    T_c = (T_f - 32.) * (5/9.)
    return T_c


@pytest.mark.parametrize("t", [(32,0), (451, 232.778)])
def test_fahrenheit2celcius(t):
    T_c = fahrenheit2celcius(t[0])
    expected_result = t[1]
    npt.assert_almost_equal(T_c, expected_result, 3)

def test_fahrenheit2celcius_type():
    with pytest.raises(TypeError):
        fahrenheit2celcius(1+1j)
