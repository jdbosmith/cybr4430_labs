# A library of functions for complex numbers, vectors, and matrices.

import math
import cmath

# ============================================================
# Complex number utilities
# ============================================================

def sumComplex(a, b):
    return a + b

def productComplex(a, b):
    return a * b

def divComplex(a, b):
    c, d = b.real, b.imag
    denom = c*c + d*d
    real = (a.real*c + a.imag*d) / denom
    imag = (a.imag*c - a.real*d) / denom
    return real + imag*1j

def modComplex(a):
    return abs(a)

def conjComplex(a):
    # Manual conjugation
    return complex(a.real, -a.imag)

def getReal(a):
    return a.real

def getImaginary(a):
    return a.imag


# ============================================================
# Polar/cartesian conversions
# ============================================================

def toPolar(c):
    r = abs(c)
    theta = math.degrees(cmath.phase(c))
    return r, theta

def toCart(mag, angle_deg):
    angle = math.radians(angle_deg)
    return mag * math.cos(angle) + mag * math.sin(angle)*1j

def multPolar(m1, a1, m2, a2):
    return (m1 * m2, a1 + a2)


# ============================================================
# Structure checks
# ============================================================

def isVector(v):
    return isinstance(v, list) and v != [] and all(isinstance(x, (int, float, complex)) for x in v)

def isMatrix(M):
    if not isinstance(M, list) or M == []:
        return False
    if not all(isinstance(row, list) for row in M):
        return False
    row_len = len(M[0])
    if not all(len(row) == row_len for row in M):
        return False
    if not all(isinstance(val, (int, float, complex)) for row in M for val in row):
        return False
    return True

def isWellFormed(m): 
    # Must not be empty
    if m == []:
        return False
    return isVector(m) or isMatrix(m)


# ============================================================
# Vector/matrix operations
# ============================================================

def matAdd(A, B):
    if not (isMatrix(A) and isMatrix(B)):
        return False
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scalarMatMult(s, M):
    if isVector(M):
        return [s * x for x in M]
    if isMatrix(M):
        return [[s * M[i][j] for j in range(len(M[0]))] for i in range(len(M))]
    return False

def scalarVecMult(s, v):
    if not isVector(v):
        return False
    return [s * x for x in v]

def vecSub(v1, v2):
    if not (isVector(v1) and isVector(v2)) or len(v1) != len(v2):
        return False
    return [v1[i] - v2[i] for i in range(len(v1))]

def isZeroVector(v, tol=1e-10):
    return all(abs(x) < tol for x in v)

def transpose(m):
    if isVector(m):
        return [[x] for x in m]
    if isMatrix(m):
        rows, cols = len(m), len(m[0])
        return [[m[r][c] for r in range(rows)] for c in range(cols)]
    return False

def conjugate(m):
    # Manual conjugation for vectors
    if isVector(m):
        return [complex(x.real, -x.imag) if isinstance(x, complex) else complex(x, -0.0) for x in m]

    # Manual conjugation for matrices
    if isMatrix(m):
        return [
            [
                complex(x.real, -x.imag) if isinstance(x, complex) else complex(x, -0.0)
                for x in row
            ]
            for row in m
        ]

    return False

def conjugTranspose(m):
    c = conjugate(m)
    if c is False:
        return False
    return transpose(c)

def matrixMult(A, B):
    if not (isMatrix(A) and isMatrix(B)):
        return False
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    if colsA != rowsB:
        return False
    result = []
    for i in range(rowsA):
        row = []
        for j in range(colsB):
            total = sum(A[i][k] * B[k][j] for k in range(colsA))
            row.append(total)
        result.append(row)
    return result

def matVecMult(M, v):
    if not (isMatrix(M) and isVector(v)):
        return False
    rows, cols = len(M), len(M[0])
    if len(v) != cols:
        return False
    return [sum(M[i][j] * v[j] for j in range(cols)) for i in range(rows)]

def innerprod(a, b):
    # Manual conjugation inside inner product
    if isVector(a) and isVector(b):
        if len(a) != len(b):
            return False
        return sum(
            complex(a[i].real, -a[i].imag) * b[i]
            for i in range(len(a))
        )

    if isMatrix(a) and isMatrix(b):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            return False
        return sum(
            complex(a[r][c].real, -a[r][c].imag) * b[r][c]
            for r in range(len(a))
            for c in range(len(a[0]))
        )

    return False

def norm_nvec(v):
    if not isVector(v):
        return False
    return math.sqrt(sum(abs(x)**2 for x in v))


# ============================================================
# Special matrices
# ============================================================

def getIdentity(n):
    if not isinstance(n, int) or n <= 0:
        return False
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def checkIdentity(M):
    if not isMatrix(M):
        return False
    n = len(M)
    if n != len(M[0]):
        return False
    for i in range(n):
        for j in range(n):
            if i == j and M[i][j] != 1:
                return False
            if i != j and M[i][j] != 0:
                return False
    return True

def getHadamard():
    scale = 1 / math.sqrt(2)
    return [[scale, scale], [scale, -scale]]

def checkHadamard(M):
    if not isMatrix(M) or len(M) != 2 or len(M[0]) != 2:
        return False
    H = getHadamard()
    return all(abs(M[i][j] - H[i][j]) < 1e-10 for i in range(2) for j in range(2))


# ============================================================
# Matrix property checks
# ============================================================

def isHermitian(M):
    if not isMatrix(M):
        return False
    n = len(M)
    for i in range(n):
        for j in range(n):
            # Manual conjugation
            if complex(M[i][j].real, -M[i][j].imag) != M[j][i]:
                return False
    return True

def isUnitary(M):
    if not isMatrix(M):
        return False
    n = len(M)
    Udagger = conjugTranspose(M)
    product = matrixMult(Udagger, M)
    if product is False:
        return False
    tol = 1e-10
    for i in range(n):
        for j in range(n):
            if i == j:
                if abs(product[i][j] - 1) > tol:
                    return False
            else:
                if abs(product[i][j]) > tol:
                    return False
    return True
