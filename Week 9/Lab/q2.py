first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
while (first_number + second_number >= 100) or first_number <= 0 or second_number <= 0:
    print("Conditions not satisfied!")
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

print("Thanks!")