from mod01_06 import innerprod, norm_nvec
import numpy

def test_innerprod():   
    assert numpy.allclose(innerprod([1 + 2j, -2 ,4j],[1j, -5+3j, 7]), (12-33j))
    
def test_norm_nvec():
    assert numpy.allclose(norm_nvec([9,3,7,1,9,4,3]), 15.684387141358123)
