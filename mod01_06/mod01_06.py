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

#helper method to check if the input is a vector
def isVector(m):
    if not isinstance(m, list):
        return False
    if m == []:
        return False
    # If any element is a list, then it's not a vector
    if any(isinstance(val, list) for val in m):
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

#  function that takes two well-formed complex vectors/matrices as its input and returns the inner product of its inputs.
def innerprod(m1, m2):
    if not (isWellFormed(m1) and isWellFormed(m2)):
        return False

    # vector inner product
    if isVector(m1) and isVector(m2):
        if len(m1) != len(m2):
            return False
        total = 0
        for a, b in zip(m1, m2):
            total += complex(a).conjugate() * b
        return total

    # matrix inner product
    if isMatrix(m1) and isMatrix(m2):
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            return False
        total = 0
        for r in range(len(m1)):
            for c in range(len(m1[0])):
                total += complex(m1[r][c]).conjugate() * m2[r][c]
        return total

    # mixed types (vector vs matrix)
    return False


#  function that takes a complex vector of size n as its input and returns the norm of its input vector.
def norm_nvec(v):
    #Complete the function
    return False
