#  function that takes two equal dimensioned complex vectors/matrices as its inputs and returns a vector/matrix that is obtained by adding its two inputs.
def matAdd(m1,m2):
    #Check if the dimensions of the two matrices are equal
    if len(m1) != len(m2):
        return False
    
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            return False
        
    # Element-wise addition
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)

    return result     

    
#  function that takes a scalar and a complex vector/matrix as its two inputs and returns a vector/matrix that is a product of its two inputs.
def scalarMatMult(m1,m2):
    #Check if the dimensions of the two matrices are compatible for multiplication 
    if not isinstance(m1, list) or not isinstance(m2, list):
        return False
    
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])
    rows_m2 = len(m2)
    cols_m2 = len(m2[0])

    if cols_m1 != rows_m2:
        return False

    result = []
    for i in range(rows_m1):
        row = []
        for j in range(cols_m2):
            s = 0
            for k in range(cols_m1):
                s += m1[i][k] * m2[k][j]
            row.append(s)
        result.append(row)

    return result
    
# function that takes a well-formed matrix/vector as its input and returns the transpose of its input.
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


# function that takes a well formed matrix/vector as its input and returns the conjugate of its input.
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


# function that applies the dagger operation on a matrix/vector and returns the result.
def conjugTranspose(m1):
    result = conjugate(m1)
    if result is False: 
        return False
    return transpose(result)
