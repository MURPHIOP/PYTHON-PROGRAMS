n = int(input("Enter the number of elements in the tuple: "))
elements = []
for i in range(n):
    item = input(f"Enter element #{i+1}: ")
    elements.append(item)

user_tuple = tuple(elements)

reversed_tuple = user_tuple[::-1]

print("\nOriginal Tuple:", user_tuple)
print("Reversed Tuple:", reversed_tuple)
