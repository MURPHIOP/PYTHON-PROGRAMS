n1 = int(input("Enter number of items in first dictionary: "))
d1 = {}
for i in range(n1):
    k = input(f"Enter key {i+1} for dict1: ")
    v = input(f"Enter value {i+1} for dict1: ")
    d1[k] = v

n2 = int(input("\nEnter number of items in second dictionary: "))
d2 = {}
for i in range(n2):
    k = input(f"Enter key {i+1} for dict2: ")
    v = input(f"Enter value {i+1} for dict2: ")
    d2[k] = v

d1.update(d2)
print("\nMerged Dictionary:", d1)


