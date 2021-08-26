# Q5
# The following function is provided to you.
# Do not modify the function definition!
def get_user_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')

# Write your code below:
user = get_user_info()

if user[2] <= 6 :
    print(f"{user[0]} You can travel for free")
elif user[2] >= 60 :
    if user[1] == "M":
        print(f"Mr. {user[0]}, you can get concessionary fare for senior citizen")
    elif user[1] == "F":
        print(f"Ms. {user[0]}, you can get concessionary fare for senior citizen")
else:
    if user[1] == "M":
        print(f"Mr. {user[0]} You need to pay full fare")
    elif user[1] == "F":
        print(f"Ms. {user[0]} You need to pay full fare")