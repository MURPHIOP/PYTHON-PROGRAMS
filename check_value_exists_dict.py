d = {}
n = int(input("Enter number of items in dictionary: "))
for i in range(n):
    k = input(f"Enter key {i+1}: ")
    v = input(f"Enter value for {k}: ")
    d[k] = v

val = input("\nEnter value to check: ")

if val in d.values():
    print("Value exists in the dictionary.")
else:
    print("Value not found in the dictionary.")
