first_matrix_type = str(input("insert the type of your first matrix, like 3x4: "))
if type(first_matrix_type) != type(str()):
    print("nope, try again")
second_matrix_type = str(input("insert the type of your second matrix, like 4x3: "))
if type(second_matrix_type) != type(str()):
    print("nope, try again")

first = first_matrix_type.split("x")
second = second_matrix_type.split("x")

matrix_1 = []
matrix_2 = []
row = []

if (len(first) == 2)and (len(second) == 2):
    if (first[1] == second[0]):
        for i in range(int(first[0])):
            first_matrix_rows = str(input("insert row {}, elements with space between them: ".format(i)))
            a = first_matrix_rows.split(" ")
            if len(a) > int(first[1]):
                print("nope")
            else:
                for number in a:
                    row.append(int(number))
                matrix_1.append(row)
                row = []
        print("your first matrix is: " + matrix_1)
        for i in range(int(second[0])):
            second_matrix_rows = str(input("insert row {}, elements with space between them: ".format(i)))
            b = second_matrix_rows.split(" ")
            if len(b) > int(second[1]):
                print("nope")
            else:
                for number in b:
                    row.append(int(number))
                matrix_2.append(row)
                row = []
    
        print("your second matrix is: " + matrix_2)
    else:
        print("first matrices column number must be equal to seconds row numbers")
else:
    print("matrices can be have rows and columns")


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

print(matrix_product(matrix_1,matrix_2))
