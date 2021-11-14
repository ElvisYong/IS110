

# # Part A
def display_all_gpas(gpas):
    print('Student Name   Student GPA')
    print('------------   -----------')
    for keys in gpas:
        print(keys, '\t\t', gpas[keys])

gpas = {'George Leung':3.4, 'Eric Wong':3.9,'Michelle Lee':3.1}

# display_all_gpas(gpas)


# # Part B
# student = input('Whose GPA do you want to change? ')
# while student not in gpas:
#     print("Sorry! This student doesn't exist")
#     student = input('Whose GPA do you want to change? ')
# new_gpa = input("What's the new GPA? ")
# gpas[student] = new_gpa
# print('Thanks! GPA has changed.')


# display_all_gpas(gpas)

# Part C
student = input('Whose GPA do you want to add? ')
while student in gpas:
    print("Sorry! This student already exist")
    student = input('Whose GPA do you want to change? ')
new_gpa = input("What's the new GPA? ")
gpas[student] = new_gpa
print('Thanks! GPA has changed.')

display_all_gpas(gpas)
