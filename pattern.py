def print_half_pyramid(n):
    if n > 0:
        print_half_pyramid(n - 1)
        print('*' * n)
rows = int(input("Enter the number of rows for the half pyramid: "))
print_half_pyramid(rows)
