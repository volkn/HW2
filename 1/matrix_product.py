def matrix_product(A,B):
    rowA = len(A)
    rowB = len(B)
    colA = len(A[0])
    colB = len(B[0])

    if colA == rowB:
        result=[[0,0,0],
                [0,0,0],
                [0,0,0]]

        for i in range(rowA):
            for j in range(colB):
                for k in range(colA):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    else:
        print("matrices cant be multiplied")

matrix1 = [[1,0,0],
           [0,1,0],
           [0,0,1]]

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,1]]

matrix3 =  [[1,2],
            [0,1],
            [0,0]]

matrix4 =  [[1,0,0],
            [1,0,2]]

print(matrix_product(matrix1,matrix2))
print(matrix_product(matrix3,matrix4))


