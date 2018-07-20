def matrix_product(A,B):
    result=[[0,0,0],
            [0,0,0],
            [0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result

matrix1 = [[1,0,0],
           [0,1,0],
           [0,0,1]]

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,1]]

print(matrix_product(matrix1,matrix2))


