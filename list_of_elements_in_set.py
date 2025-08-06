s = set()
n = int(input("Enter number of elements: "))
for i in range(n):
    x = input(f"Enter element {i+1}: ")
    s.add(x)

print("\nSet created:", s)

l = list(s)
print("Elements as list:", l)
