#helper function to check if a vector or matrix is well-formed
def isWellFormed(m):
    # Must be a list
    if not isinstance(m, list):
        return False

    # Must not be empty
    if m == []:
        return False

    # CASE 1: Vector (1D list of numbers)
    if all(isinstance(val, (int, float, complex)) for val in m):
        return True

    # CASE 2: Matrix (list of lists)
    if not all(isinstance(row, list) for row in m):
        return False

    # Must be rectangular
    row_length = len(m[0])
    if not all(len(row) == row_length for row in m):
        return False

    # All entries must be numeric
    for row in m:
        for val in row:
            if not isinstance(val, (int, float, complex)):
                return False

    return True

#helper method to check if the input is a matrix
def isMatrix(m):
    if not isinstance(m, list):
        return False
    if m == []:
        return False
    if not all(isinstance(row, list) for row in m):
        return False
    # Must be rectangular
    row_length = len(m[0])
    if not all(len(row) == row_length for row in m):
        return False

    return True

# helper function that takes a well formed matrix/vector as its input and returns the conjugate of its input.
def conjugate(m1):
    # Validate matrix structure
    if not isinstance(m1, list):
        return False
    if not all(isinstance(row, list) for row in m1):
        return False

    result = []
    for row in m1:
        new_row = []
        for elem in row:
            if isinstance(elem, complex):
                new_row.append(complex(elem.real, -elem.imag))
            elif isinstance(elem, (int, float)):
                # Real numbers become a complex with -0j
                new_row.append(complex(elem, -0.0))
            else:
                return False
        result.append(new_row)
    return result

# helperfunction that takes a well-formed matrix/vector as its input and returns the transpose of its input.
def transpose(m1):
    # check that m1 is a list
    if not isinstance(m1, list):
        return False

    # check that m1 is a list of lists
    if not all(isinstance(row, list) for row in m1):
        return False

    # Matrix must be rectangular
    row_len = len(m1[0])
    if not all(len(row) == row_len for row in m1):
        return False

    # Compute transpose: P^T[j][k] = P[k][j]
    rows = len(m1)
    cols = len(m1[0])

    T = []
    for j in range(cols):
        new_row = []
        for k in range(rows):
            new_row.append(m1[k][j])
        T.append(new_row)

    return T

# helper function that applies the dagger operation on a matrix/vector and returns the result.
def conjugTranspose(m1):
    result = conjugate(m1)
    if result is False: 
        return False
    return transpose(result)

#helper function that takes two well-formed complex vectors/matrices as its input multiplies them.
def matrixMult(M1, M2):
    if not (isWellFormed(M1) and isMatrix(M1) and
            isWellFormed(M2) and isMatrix(M2)):
        return False

    rows1 = len(M1)
    cols1 = len(M1[0])
    rows2 = len(M2)
    cols2 = len(M2[0])

    if cols1 != rows2:
        return False

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += M1[i][k] * M2[k][j]
            row.append(total)
        result.append(row)

    return result

#  function that takes a well-formed matrix with real/complex entries as its input and outputs true if the input matrix is Hermitian and outputs false if the matrix is not Hermitian.
def isHermitian(m):
    #Check if the input is a well-formed matrix
    if not (isWellFormed(m) and isMatrix(m)):
        return False
    # Check if the matrix is square
    num_rows = len(m)
    if num_rows == 0:
        return False
    num_cols = len(m[0])
    if num_rows != num_cols:
        return False

    #Hermitian matrix: An 𝑛×𝑛 matrix is called hermitian if 𝐴^†=𝐴.
    # Check if the matrix is Hermitian
    for i in range(num_rows):
        for j in range(num_cols):
            if complex(m[i][j]).conjugate() != m[j][i]:
                return False

    return True

#  function takes a well-formed matrix with real/complex entries as its input and outputs true if the input matrix is unitary and outputs false if the input matrix is not unitary.
def isUnitary(m):
    #Check if the input is a well-formed matrix
    if not (isWellFormed(m) and isMatrix(m)):
        return False

    # Check if the matrix is square
    n = len(m)
    if n == 0 or len(m[0]) != n:
        return False

    #Unitary Matrix: An 𝑛×𝑛 matrix is unitary if 𝑈𝑈^†=𝑈^†𝑈=𝐼.
    # Compute conjugate transpose
    Udagger = conjugTranspose(m)
    if Udagger is False:
        return False

    # Multiply Udagger * U
    product = matrixMult(Udagger, m)
    if product is False:
        return False

    # Check if product is identity
    tolerance = 1e-10

    for i in range(n):
        for j in range(n):
            val = product[i][j]

            if i == j:
                if abs(val - 1) > tolerance:
                    return False
            else:
                if abs(val) > tolerance:
                    return False
    return True
