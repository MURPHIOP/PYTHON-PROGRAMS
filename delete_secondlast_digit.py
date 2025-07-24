number = input("Enter a number: ")
if len(number) >= 2:
    second_last = number[-2]
    print(f"The second last digit of {number} is {second_last}")
else:
    print(f"The number {number} has less than 2 digits.")



print("The program is running properly")
