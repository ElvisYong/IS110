from random import randint
a = randint(1, 9)
b = randint(1, 9)
practice = input("Do you want to practice multiplication table? Please enter Y or N: ")
user_ans = float(input(f"What's the result of {a} times {b}? "))

while practice == "Y":
    while user_ans != a * b:
        user_ans = float(input(f"Wrong answer! Please try again: "))
    print("You are right!")
    practice = input("Do you want to continue your practice? Please enter Y or N: ")   
    if practice == "Y":
        a = randint(1, 9)
        b = randint(1, 9)
        user_ans = float(input(f"What's the result of {a} times {b}? "))

