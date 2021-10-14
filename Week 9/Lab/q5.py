first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

while any(char.isspace() for char in first_string) or any(char.isspace() for char in second_string) or len(second_string) <= len(first_string) or not all(char in first_string for char in second_string):
    print("Conditions not satisfied!")
    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")