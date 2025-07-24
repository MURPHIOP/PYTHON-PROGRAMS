arr = []
for i in range(0,3):
    a=[]
    for j in range(0,3):
        name = int(input("Enter the number:"))
        a.append(name)
    arr.append(a)
for i in range (0,3):
    for j in range(0, 3):
        print(arr[i][j], end=" ")
    print("\n")
