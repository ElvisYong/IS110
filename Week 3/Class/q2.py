def get_day_of_week(n):
    if n == 0:
        return "Sunday"
    elif n == 1:
        return "Monday"
    elif n == 2:
        return "Tuesday"
    elif n == 3:
        return "Wednesday"
    elif n == 4:
        return "Thursday"
    elif n == 5:
        return "Friday"
    elif n == 6:
        return "Saturday"
    else:
        return "Error"


day = int(input("Enter a number 0-6: "))
if day < 0:
    print("Your number should be at least 0")
elif day > 6:
    print("Your number should be at most 6")

print(get_day_of_week(day))
