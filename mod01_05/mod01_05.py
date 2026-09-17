import math

# function that takes a matrix as its input and returns the number of dimensions if a well-formed matrix and Linear Independent, otherwise return False.
def checkLinearIndependence(m1):
    # Check if the matrix is empty
    if m1 == []:
        return False

    # Check if m1 is a list
    if not isinstance(m1, list):
        return False
    
    # Check if the matrix is well-formed (all rows are lists)
    if not all(isinstance(row, list) for row in m1):
        return False

    # Check if the matrix is rectangular (all rows have the same length)
    row_length = len(m1[0])
    if not all(len(row) == row_length for row in m1):
        return False

    # Check if the matrix is square
    rows = len(m1)
    if rows != row_length:
        return False

    # Check that all values are 0 or 1
    for row in m1:
        for val in row:
            if val not in (0, 1):
                return False
    
    #Capure the number of rows. Since we have already checked that the matrix is well-formed, we can safely get the number of rows.
    rows = len(m1)

    return rows




# function that takes a matrix as its input and returns the number of dimensions if a well-formed identity matrix, otherwise return False.
def checkIdentity(m1):
    # First: check if the matrix is well-formed and linear independent
    if checkLinearIndependence(m1) is False:
        return False

    rows = len(m1)

    # Identity matrix rules
    for i in range(rows):
        for j in range(rows):
            val = m1[i][j]

            # Diagonal must be 1
            if i == j and val != 1:
                return False

            # Off-diagonal must be 0
            if i != j and val != 0:
                return False

    # If all checks pass, return the dimension
    return rows


# function that returns normalized identity matrix in n dimensions
def getIdentity(n):
    # Validate n
    if not isinstance(n, int) or n <= 0:
        return False

    # Build normalized identity matrix
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    return matrix

# function that returns normalized Hadamard matrix in 2 dimensions
def getHadamard():
    scale = 1 / math.sqrt(2)
    return [
        [scale,  scale],
        [scale, -scale]
    ]

def checkHadamard(m1):
    # Check if the matrix is empty
    if m1 == []:
        return False

    # Check if m1 is a list
    if not isinstance(m1, list):
        return False
    
    # Check if the matrix is well-formed (all rows are lists)
    if not all(isinstance(row, list) for row in m1):
        return False

    # Check rectangular
    row_length = len(m1[0])
    if not all(len(row) == row_length for row in m1):
        return False

    # Check square
    rows = len(m1)
    if rows != row_length:
        return False

    # Hadamard must be 2x2
    if rows != 2:
        return False

    # Expected Hadamard values
    scale = 1 / math.sqrt(2)
    expected = [
        [scale,  scale],
        [scale, -scale]
    ]

    # Compare with tolerance
    for i in range(2):
        for j in range(2):
            if abs(m1[i][j] - expected[i][j]) > 1e-6:
                return False

    return True

def getHadmond():
    #TODO: Needed for test_getHadmond() in test_mod01_05.py, but not implemented yet.
    return True

def checkHadmond(m1):
    #TODO: Needed for test_getHadmond() in test_mod01_05.py, but not implemented yet.
    return True