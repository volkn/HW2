import sys

f = open("matrix.txt","r+")
f2 = open("output.txt","w+")
t = 0
info = []
type_m = []
text = f.read()
text = text.rstrip('\n')
if text[0] != "[" and text[-1] != "]":
    sys.exit("you should insert matrices")
matrix_list = []


how_many_matrix = 0
for i in text:
    if i == "*":
        how_many_matrix += 1

if how_many_matrix == 0:
    sys.exit("you should insert matrices, more than one.")

mlist = text.strip()
matrix_list = mlist.split("*")

#for i in matrix_list:
#    if i[]
for i in matrix_list:
    for j in range(len(i)):
        if type(i[j]) == type(int()) or i[j] == "]" or i[j] == "[" or i[j] == ",":
            pass
        elif i[j] == ".":
            try:
                if type(eval(i[j+1])) == type(int()):
                    pass
            except:
                sys.exit("you can only put numbers in matrices")
        else:
            try:
                if type(eval(i[j])) == type(int()):
                    pass
            except:
                sys.exit("you can only put numbers in matrices")
a = 0
b = 0
c = 0
matrix_types = []
for i in matrix_list:
    for char in i:
        if char == "[":
            a += 1
        elif char == "]":
            b += 1
        elif char == ",":
            c += 1
    c = c+1
    if a != b:
        sys.exit("your row's are wrong")
    c = c / (a - 1)
    c = int(c)
    mat_type = [a-1,c]
    matrix_types.append(mat_type)
    del mat_type
    a = 0
    b = 0
    c = 0

for i in range(len(matrix_types)):
    if i == len(matrix_types) - 1:
        break
    elif matrix_types[i][1] != matrix_types[i+1][0]:
        sys.exit("your matrix types are not good for multiplying")

print("matrix types")
print(matrix_types)

true_mat_list = []
for i in matrix_list:
    try:
        if type(eval(i)) == type([]):
            true_mat_list.append(eval(i))
    except:
        sys.exit("nope")

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
s = 0
try:
    for i in range(how_many_matrix):
        s += 1
        if res == []:
            res = matrix_product(true_mat_list[0],true_mat_list[1])
        else:
            res = matrix_product(res,true_mat_list[i])
    print(res)
    print(res,file=f2)
    f.close()
    f2.close()
except:
    sys.exit("some unexpected mistake")


##############################################################


question = int(input("How many matrix do you wont "))
matrices = []
test = f.read()
if type(text[29] == type(int()):
        try:
            question = int(text[29])
            matrices = 

for i in range(question):
    M_type  = str(input("insert the type of your first matrix, like 3x4: "))
    while M_type[0] != type(int()) and type(M_type[2] ) != type(int()) and M_type[1] != "x":
        M_type = str(input("insert the type of your first matrix again, like 3x4: "))
    matrices.append(M_type)

print("your matrix types: ",matrices)
print("your matrix types: ",matrices, file = f,flush=True)

a = 0
while True:
    if matrices[a][-1] != matrices[a+1][0]:
        print("your matrices cant be multiplied")
        sys.exit("start from the begining")
    else:
        a = a + 1
        if a == len(matrices) -1:
            break


matrix_1 = []
matrix_2 = []
row = []

matrixTypeList = []
for i in matrices:
    thing = i.split("x")
    matrixTypeList.append(thing)


lastMatrixList = []
for matrix_indicator in range(len(matrices)):
    fullMatrix = []
    for i in range(int(matrixTypeList[matrix_indicator][0])):
        matrix_rows = str(input("insert row {}'s, elements with space between them: ".format(i)))
        a = matrix_rows.split(" ")
        while True:
            if len(a) == int(matrixTypeList[matrix_indicator][1]):
                print("oket now you can insert the next row")
                break
            else:
                print("you can only insert rows, now insert first matrix from the first row")
                matrix_rows = str(input("insert row {}, elements with space between them: ".format(i)))
                a = matrix_rows.split(" ")
        row = []
        for number in a:
            row.append(int(number))
        fullMatrix.append(row)
        row = []
    lastMatrixList.append(fullMatrix)

print("your matrices", lastMatrixList)
print("your matrices", lastMatrixList, file = f,flush=True)

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

def operate(a=2, result_matrix=matrix_product(lastMatrixList[0], lastMatrixList[1])):
    if a == len(lastMatrixList):
        print("result is: ",result_matrix)
        print("result is: ",result_matrix, file = f,flush=True):
    else:
        result_matrix = matrix_product(result_matrix,lastMatrixList[a])
        a = a + 1
        operate(a, result_matrix)

operate()
f.close()

