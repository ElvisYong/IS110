number = int(input("Enter an integer: "))
all_numbers = ''
while number >= 0:
    if number % 2 != 0:
        if all_numbers == '':
            all_numbers = all_numbers + str(number)
        else:
            all_numbers = all_numbers + ', ' + str(number)
    number = int(input("Enter an integer: "))

print("Thanks")
print("The ood positive integers you have entered are the following: " + all_numbers)