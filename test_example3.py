import pytest
import numpy.testing as npt

# contents of test_example3.py
def fahrenheit2celcius(T_f):
    """
    Convert temperature in Fahrenheit to Celcius
    """
    T_c = (T_f - 32.) * (5/9.)
    return T_c


@pytest.mark.parametrize("t", [(32,0), (451, 232.778)])
def test_fahrenheit2celcius(t):
    T_c = fahrenheit2celcius(t[0])
    expected_result = t[1]
    npt.assert_almost_equal(T_c, expected_result, 3)

