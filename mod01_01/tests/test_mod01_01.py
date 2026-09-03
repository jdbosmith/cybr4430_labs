from mod01_01 import sumComplex, productComplex, getReal, getImaginary

def test_sumComplex():   
    assert sumComplex(1+2j, 3-1j) == 4 + 1j
    assert sumComplex(-1+5j, 2-3j) == 1 + 2j
    assert sumComplex(0+0j, 0+0j) == 0 + 0j    

def test_productComplex():
    assert productComplex(-20 + -12j, 13 + 16j) == (-68 - 476j)
    assert productComplex(0+0j, 7-2j) == 0+0j

def test_getReal():
    assert getReal(3 + 4j) == 3
    assert getReal(-5+0j) == -5.0
    assert getReal(0+2j) == 0.0

def test_getImaginary():
    assert getImaginary(0-7j) == -7.0
    assert getImaginary(3+4j) == 4.0
    assert getImaginary(-5+0j) == 0.0
