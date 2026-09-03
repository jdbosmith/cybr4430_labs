from mod01_03 import toPolar, toCart, multPolar
from math import isclose

def test_toPolar():   
    assert toPolar(-6) == (6,180)

def test_toCart():
    assert isclose(toCart(3.6055512754639896,56.309932474020215).real, 2) and isclose(toCart(3.6055512754639896,56.309932474020215).imag, 3)

def test_multPolar():
    assert isclose(multPolar(5, 30, 4, -45)[0],20) and isclose(multPolar(5, 30, 4, -45)[1],-15)
