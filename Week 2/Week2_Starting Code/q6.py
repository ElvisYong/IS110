from week2_utility import get_insurance_premium

# age = int(input("How old are you? "))
# gender = input("What is your gender? ")

# print(get_insurance_premium(age, gender))

age = int(input(f"age: "))
gender = input(f"Gender(M/F): ")

print(f"The amount of insurance is: {get_insurance_premium(age, gender)}")
