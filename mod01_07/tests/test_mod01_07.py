from mod01_07 import isHermitian, isUnitary
import numpy

def test_isHermitian():   
    assert isHermitian([[1,2-1j],[2 + 1j, 0]]) == True
    
def test_isUnitary():
    assert isUnitary([[.5+.5j,.5+.5j],[.5-.5j,-.5 + .5j]]) == True
    
