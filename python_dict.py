n = int(input("Enter how many numbers you want: "))

keys = []
values = []

for i in range(1, n + 1):
    keys.append(i)

for i in keys:
    values.append(i ** 2)

squares_dict = {}

for i in range(len(keys)):
    squares_dict[keys[i]] = values[i]

print("Dictionary of numbers and their squares:")
print(squares_dict)
