first_matrix_type = str(input("insert the type of your first matrix, like 3x4: "))

while first_matrix_type[0] != type(int()) and type(first_matrix_type[2] ) != type(int()) and first_matrix_type[1] != "x":
    first_matrix_type = str(input("insert the type of your first matrix again, like 3x4: "))

second_matrix_type = str(input("insert the type of your second matrix, like 4x3: "))
while second_matrix_type[0] != type(int()) and type(second_matrix_type[2] ) != type(int()) and second_matrix_type[1] != "x":
    second_matrix_type = str(input("insert the type of your second matrix again, like 3x4: "))

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
            while True:
                if len(a) == int(first[1]):
                    print("okkey now you can insert the next row")
                    break
                else:
                    print("you can only instert rows, now insert first matrix from the first row")
                    first_matrix_rows = str(input("insert row {}, elements with space between them: ".format(i)))
                    a = first_matrix_rows.split(" ")

            for number in a:
                row.append(int(number))
            matrix_1.append(row)
            row = []
    
        for i in range(int(second[0])):
            second_matrix_rows = str(input("insert row {}, elements with space between them: ".format(i)))
            b = second_matrix_rows.split(" ")
            while True:
                if len(b) == int(second[1]):
                    print("okkey now you can insert the next row")
                    break
                else:
                    print("you can only instert rows, now insert second matrix from the first row")
                    second_matrix_rows = str(input("insert row {}, elements with space between them: ".format(i)))
                    b = second_matrix_rows.split(" ")

            for number in b:
                row.append(int(number))
            matrix_2.append(row)
            row = []
    
    else:
        print("first matrices column number must be equal to seconds row numbers")
    
else:
        print("matrices can be have rows and columns")

print("your first matrix is: {}".format(matrix_1))
print("your second matrix is: {}".format(matrix_2))

def matrix_product(A,B):
    rowA = len(A)
    rowB = len(B)
    colA = len(A[0])
    colB = len(B[0])

    if colA == rowB:
        result = []
        for i in range(rowA):
            result_row = []
            for k in range(colB):
                result_row.append(0)
            result.append(result_row)

        for i in range(rowA):
            for j in range(colB):
                for k in range(colA):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    else:
        print("matrices cant be multiplied")

print(matrix_product(matrix_1,matrix_2))
