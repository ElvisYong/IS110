# 1a)
age = int(input("Enter your age (between 0 and 100, both inclusive): "))

while age > 100 or age < 0:
    print("Please enter a valid age!")
    age = int(input("Enter your age (between 0 and 100, both inclusive): "))

print("Thanks!")

# 1b)
student = input("Are you a student? ")

while student != "YES" or student != "Yes" or student != "yes" or student != "NO" or student != "No" or student != "no":
    print("Please enter a valid answer! (YES, Yes, yes, NO, No or no")
    student = input("Are you a student? ")
print("Got it")

#1c)
def isInvalid(string):
    if any(not (char.isalpha() or char.isspace()) for char in string):
        return True
    return False

name = input("Enter your name: ")
while isInvalid(name):
    print("Please enter a valid name!")
    name = input("Enter your name: ")
print("Thanks!")