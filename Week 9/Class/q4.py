pin = input("Enter pin: ")
confirm = input("Confirm your new pin: ")

while (pin != confirm) or (len(pin) != 6) or (any(not char.isdigit() for char in pin)):
    print("Sorry! There is an error! The following errors are detected: ")
    if pin != confirm:
        print("- The pin and confirm pin are not the same!")
    if len(pin) > 6:
        print("- The pin is too long!")
    if len(pin) < 6:
        print("- The pin is too short!")
    if any(not char.isdigit() for char in pin):
        print("- The pin contains non-digit characters!")
    pin = input("Enter pin: ")
    confirm = input("Confirm your new pin: ")

print("Thanks! Your new PIN has been set!")
