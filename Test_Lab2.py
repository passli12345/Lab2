import pytest
from Lab2 import calc_min_max_temperature, calc_average_temperature, calc_median_temperature
import Lab2

def test_calc_min_max_temperature():
    assert calc_min_max_temperature([5.0, 69.0, 32.0]) == [5.0, 69.0]
    assert calc_min_max_temperature([-10.5, 0.0, 10.5]) == [-10.5, 10.5]

def test_calc_average_temperature():
    assert calc_average_temperature([5.0, 69.0, 32.0]) == pytest.approx(35.33, 0.01)
    assert calc_average_temperature([10.0, 20.0, 30.0]) == pytest.approx(20.0, 0.01)

def test_calc_median_temperature():
    result = 0
    input_list = [5, 15, 25, 35, 45]
    except_result = 25
    result = Lab2.calc_median_temperature(input_list)
    assert result == except_result
