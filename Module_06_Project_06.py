#Tri Dinh 
"""
Write a Python program that receives two matrices to check if they are inverse one to each other.

    ● Your program should them verify if the two matrices are the inverse of the other

        ○ Multiply the matrices to confirm:

            ● If the matrices cannot be multiplied, them they are not inverses to each other;

            ● If their multiplication does not give an Identity matrix, they are not inverses to each other.
"""
def mulitple_matrix(A, B):
    if len(A[0]) != len(B):
        return False
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(B)):
                tmp += A[i][k] * B[k][j]
            C[-1].append(tmp)
    return C


def identity_matrix_check(C):
    if len(C) != len(C[0]):
        return False
    else:
        for i in range(len(C)):
            if C[i][i] != 1:
                return False
            for j in range(len(C[0])):
                if i == j:
                    continue
                if C[i][j] != 0:
                    return False
    
    return True

#read file
input_file = open('input.txt', 'r')
a = []
b = []
current = a #current matrix

for line in input_file.readlines():
    #This is our separator - a line with no ',', switch a matrix
    if ',' not in line: 
        current = b
    else:
        #Add a row to current matrix
        current.append([])
        #Values are separated by ','
        for x in line.split(','):
            #Add int(x) to the last line
            current[len(current) - 1].append((float(x)))


F = mulitple_matrix(a,b)
if F == False:
    print("these two matrices can't be multipled so the matrices are not inverses to each other\n")
    print(a)
    print(b)
else:
    #rounding
    for i in range(len(F)):
        for j in range(len(F[0])):
            if F[i][j] < 0.01 :
                F[i][j] = round(F[i][j], 2)

    if identity_matrix_check(F) == True:
        print("the matrices are inverses to each other\n")
        print(a)
        print(b)
    else:
        print("the matrices are not inverses to each other\n")
        print(a)
        print(b)

input_file.close()