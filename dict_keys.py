n = int(input("Enter how many key-value pairs you want: "))

my_dict = {}

for i in range(n):
    key = input(f"Enter letter key #{i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value

print("\nYour dictionary:")
print(my_dict)

print("\nAll possible 2-letter combinations of dictionary keys:")
keys = list(my_dict.keys())

for i in range(len(keys)):
    for j in range(len(keys)):
        if i != j:
            print(keys[i] + keys[j])
