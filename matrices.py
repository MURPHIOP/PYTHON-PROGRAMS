R= int(input("ENTER THE NUMBER OF ROWS"))
C=int(input("ENTER THE NUMBER OF COLUMNS"))



matrix=[]
for i in range (R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

for i in range(R):
    for j in range(C):
        print(matrix[j][i], end = " ")
    print()

