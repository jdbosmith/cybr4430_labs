from mod01_08 import tensor
import numpy

def test_tensor():   
    assert numpy.allclose(tensor([1,2j],[2+3j,4]), [(2+3j), (4+0j), (-6+4j), 8j])  #Vector
    assert numpy.allclose(tensor([[3,4j],[1+7j,0]],[2-17j,4]),[[(6-51j), (68+8j)], [(12+0j), 16j], [(121-3j), 0j], [(4+28j), 0j]]) #Matrix and Vector
