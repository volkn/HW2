import sys

f = open("matrix.txt","r+")
t = 0
info = []
type_m = []
text = f.read()
#mList = text.split(",")
#print(mList)
matrix_list = []

how_many_matrix = 0
for i in text:
    if i == "*":
        how_many_matrix += 1

a = 0
for i in text:
    if i == "[":
        a = a + 1

#mlist = text.replace("[","",12)
mlist = text.strip()
matrix_list = mlist.split("*")
b = 0
for i in matrix_list[0]:
    if i != "]":
        b += 1
    else:
        break
true_mat_list = []
for i in matrix_list:
    if type(eval(i)) == type([]):
        true_mat_list.append(eval(i))

def matrix_product(A,B):
    rowA = len(A)
    rowB = len(B)
    colA = len(A[0])
    colB = len(B[0])

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

res = []

for i in range(how_many_matrix + 1):
    if res == []:
        res = matrix_product(true_mat_list[i],true_mat_list[i+1])
    else:
        res = matrix_product(res,true_mat_list[i])

print(res)


#question = int(input("How many matrix do you wont "))
#matrices = []
#test = f.read()
#if type(text[29] == type(int()):
#        try:
#            question = int(text[29])
#            matrices = 
#
#for i in range(question):
#    M_type  = str(input("insert the type of your first matrix, like 3x4: "))
#    while M_type[0] != type(int()) and type(M_type[2] ) != type(int()) and M_type[1] != "x":
#        M_type = str(input("insert the type of your first matrix again, like 3x4: "))
#    matrices.append(M_type)
#
#print("your matrix types: ",matrices)
#print("your matrix types: ",matrices, file = f,flush=True)
#
#a = 0
#while True:
#    if matrices[a][-1] != matrices[a+1][0]:
#        print("your matrices cant be multiplied")
#        sys.exit("start from the begining")
#    else:
#        a = a + 1
#        if a == len(matrices) -1:
#            break
#
#
#matrix_1 = []
#matrix_2 = []
#row = []
#
#matrixTypeList = []
#for i in matrices:
#    thing = i.split("x")
#    matrixTypeList.append(thing)
#
#
#lastMatrixList = []
#for matrix_indicator in range(len(matrices)):
#    fullMatrix = []
#    for i in range(int(matrixTypeList[matrix_indicator][0])):
#        matrix_rows = str(input("insert row {}'s, elements with space between them: ".format(i)))
#        a = matrix_rows.split(" ")
#        while True:
#            if len(a) == int(matrixTypeList[matrix_indicator][1]):
#                print("oket now you can insert the next row")
#                break
#            else:
#                print("you can only insert rows, now insert first matrix from the first row")
#                matrix_rows = str(input("insert row {}, elements with space between them: ".format(i)))
#                a = matrix_rows.split(" ")
#        row = []
#        for number in a:
#            row.append(int(number))
#        fullMatrix.append(row)
#        row = []
#    lastMatrixList.append(fullMatrix)
#
#print("your matrices", lastMatrixList)
#print("your matrices", lastMatrixList, file = f,flush=True)
#
#def matrix_product(A,B):
#    rowA = len(A)
#    rowB = len(B)
#    colA = len(A[0])
#    colB = len(B[0])
#
#    result = []
#    for i in range(rowA):
#        result_row = []
#        for k in range(colB):
#            result_row.append(0)
#        result.append(result_row)
#
#    for i in range(rowA):
#        for j in range(colB):
#            for k in range(colA):
#                result[i][j] += A[i][k] * B[k][j]
#    return result
#
#def operate(a=2, result_matrix=matrix_product(lastMatrixList[0], lastMatrixList[1])):
#    if a == len(lastMatrixList):
#        print("result is: ",result_matrix)
#        print("result is: ",result_matrix, file = f,flush=True):
#    else:
#        result_matrix = matrix_product(result_matrix,lastMatrixList[a])
#        a = a + 1
#        operate(a, result_matrix)
#
#operate()
#f.close()
#
