# contents of test_example5.py
import pytest
import numpy.testing as npt
import numpy as np

def celcius2fahrenheit(T_c):
    """
    Convert temperature in Fahrenheit to Celcius
    """
    if not np.isreal(T_c):
        raise TypeError("Temperature needs to be a real value")
    T_f = 9/5* T_c  + 32.
    return T_f

def fahrenheit2celcius(T_f):
    """
    Convert temperature in Fahrenheit to Celcius
    """
    if not np.isreal(T_f):
        raise TypeError("Temperature needs to be a real value")
    T_c = (T_f - 32.) * (5/9.)
    return T_c

class TestConversionf2c(object):
    @pytest.mark.parametrize("t", [(32,0), (451, 232.778)])
    def test_value(self, t):
        T_c = fahrenheit2celcius(t[0])
        expected_result = t[1]
        npt.assert_almost_equal(T_c, expected_result, 3)

    def test_type(self):
        with pytest.raises(TypeError):
            fahrenheit2celcius(1+1j)


class TestConversionc2f(object):
    @pytest.mark.parametrize("t", [(0, 32), ( 232.778, 451)])
    def test_value(self, t):
        T_c = celcius2fahrenheit(t[0])
        expected_result = t[1]
        npt.assert_almost_equal(T_c, expected_result, 3)

    def test_type(self):
        with pytest.raises(TypeError):
            celcius2fahrenheit(1+1j)
