keys = input("Enter keys list: ").split()
values = input("Enter values list: ").split()

if len(keys) != len(values):
    print("Error: Should be same length")
else:
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    print("Resulting Dictionary:", d)
