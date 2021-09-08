def password_check(password):
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char in '!@#$%^&*()' for char in password):
        return False
    else:
        return True

password = input("Enter password: ")
print(password_check(password))