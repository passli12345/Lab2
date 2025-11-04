import pytest
from Lab2 import calc_min_max_temperature, calc_average_temperature, calc_median_temperature

def test_calc_min_max_temperature():
    assert calc_min_max_temperature([5.0, 69.0, 32.0]) == [5.0, 69.0]
    assert calc_min_max_temperature([-10.5, 0.0, 10.5]) == [-10.5, 10.5]

def test_calc_average_temperature():
    assert calc_average_temperature([5.0, 69.0, 32.0]) == pytest.approx(35.33, 0.01)
    assert calc_average_temperature([10.0, 20.0, 30.0]) == pytest.approx(20.0, 0.01)

def test_calc_median_temperature():
    assert calc_median_temperature([5.0, 69.0, 32.0]) == 32.0  # Odd count
    assert calc_median_temperature([5.0, 32.0, 69.0, 100.0]) == pytest.approx(50.5, 0.01)  # Even count
