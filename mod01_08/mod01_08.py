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

#  function that take two well-formed matrices with real/complex entries and outputs the tensor product of is inputs.
def tensor(m1, m2):
    if not (isWellFormed(m1) and isWellFormed(m2)):
        return False

    # Matrix x Matrix
    if isMatrix(m1) and isMatrix(m2):
        rows1, cols1 = len(m1), len(m1[0])
        rows2, cols2 = len(m2), len(m2[0])

        tensor_val = []
        for i in range(rows1):
            for k in range(rows2):
                row = []
                for j in range(cols1):
                    for l in range(cols2):
                        row.append(m1[i][j] * m2[k][l])
                tensor_val.append(row)
        return tensor_val

    # Vector x Matrix
    elif isVector(m1) and isMatrix(m2):
        rows2, cols2 = len(m2), len(m2[0])

        tensor_val = []
        for i in range(len(m1)):
            for j in range(rows2):
                row = []
                for k in range(cols2):
                    row.append(m1[i] * m2[j][k])
                tensor_val.append(row)
        return tensor_val

    # Matrix x Vector
    elif isMatrix(m1) and isVector(m2):
        rows1, cols1 = len(m1), len(m1[0])

        tensor_val = []
        for i in range(rows1):
            for k in range(len(m2)):
                row = []
                for j in range(cols1):
                    row.append(m1[i][j] * m2[k])
                tensor_val.append(row)
        return tensor_val

    # Vector x Vector
    elif isVector(m1) and isVector(m2):
        tensor_val = []
        for i in range(len(m1)):
            for j in range(len(m2)):
                tensor_val.append(m1[i] * m2[j])
        return tensor_val


    return False
