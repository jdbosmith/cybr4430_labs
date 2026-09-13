from mod01_04 import matAdd, scalarMatMult, transpose, conjugate, conjugTranspose
import numpy

def test_matAdd():   
    assert numpy.allclose(matAdd([[4,6],[0,0]],[[1,2],[3,4]]), [[5,8],[3,4]])
    
def test_scalarMatMult():
    assert numpy.allclose(scalarMatMult(3j,[[1,3,4],[4,5,6j],[7,8,9]]), [[(0+3j), (0+9j), (0+12j)], [(0+12j), (0+15j), (-18+0j)], [(0+21j), (0+24j), (0+27j)]])
    assert numpy.allclose(scalarMatMult(4,[[9,8,7j],[6,5,4],[3,2j,1]]), [[(36+0j), (32+0j), (0+28j)], [(24+0j), (20+0j), (16+0j)], [(12+0j), (0+8j), (4+0j)]])

def test_transpose():
    assert numpy.allclose(transpose([[1,3,4],[4,5,6j],[7,8,9]]), [[1, 4, 7], [3, 5, 8], [4, 6j, 9]])

def test_conjugate():
    assert numpy.allclose(conjugate([[5+2j,6-1j],[7,8+3j]]), [[(5-2j), (6+1j)], [(7-0j), (8-3j)]])

def test_conjugTranspose():
    assert numpy.allclose(conjugTranspose([[4+2j,5+6j],[6+1j,7]]), [[(4-2j), (6-1j)], [(5-6j), (7-0j)]])
