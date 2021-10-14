from random import randint

rand_number = randint(1, 100)
number = int(input("Enter your guess (Between 1 and 100): "))

while number != rand_number:
    if number > rand_number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    number = int(input("Enter your guess (Between 1 and 100): "))

print("Bingo!")