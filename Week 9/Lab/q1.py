gender = input('Whats your gender? Please enter M or F: ')
while gender != "M" and gender != "F":
    print("Wrong input!")
    gender = input('Whats your gender? Please enter M or F: ')

if gender == "M":
    print("Thanks! Your gender is male")
else:
    print("Thanks! Your gender is female")