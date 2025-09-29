from mod01_02 import divComplex, modComplex, conjComplex

def test_divComplex():   
    assert divComplex(-20 + 12j, -13 + -16j) == (0.16-1.12j)

def test_modComplex():
    assert modComplex(-3+4j) == 5

def test_conjComplex():
    assert conjComplex(3 + 2j) == 3 - 2j
