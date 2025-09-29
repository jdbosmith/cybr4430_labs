from mod01_04 import matAdd, scalarMatMult, transpose, conjugate, conjugTranspose
import numpy

def test_matAdd():   
    assert numpy.allclose(matAdd([[4,6],[0,0]],[[1,2],[3,4]]), [[5,8],[3,4]])
    
def test_scalarMatMult():
    assert numpy.allclose(scalarMatMult([[1,3,4],[4,5,6j],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]), [[(39+0j), (31+0j), (23+0j)], [(66+18j), (57+12j), (48+6j)], [(138+0j), (114+0j), (90+0j)]])

def test_transpose():
    assert numpy.allclose(transpose([[1,3,4],[4,5,6j],[7,8,9]]), [[1, 4, 7], [3, 5, 8], [4, 6j, 9]])

def test_conjugate():
    assert numpy.allclose(conjugate([[5+2j,6-1j],[7,8+3j]]), [[(5-2j), (6+1j)], [(7-0j), (8-3j)]])

def test_conjugTranspose():
    assert numpy.allclose(conjugTranspose([[4+2j,5+6j],[6+1j,7]]), [[(4-2j), (6-1j)], [(5-6j), (7-0j)]])
