# Name:
# Email ID:

def check_math(list_of_equations):
    # Replace the code below with your implementation.
    if list_of_equations:
        for equation_in_str in list_of_equations:
            if "+" in equation_in_str:
                first_number, remainding = equation_in_str.split("+")
                second_number, ans = remainding.split("=")
                if int(first_number) + int(second_number) == int(ans):
                   return True
                return False
            elif "-" in equation_in_str:
                first_number, remainding = equation_in_str.split("-")
                second_number, ans = remainding.split("=")
                if int(first_number) - int(second_number) == int(ans):
                   return True
                return False
            elif "*" in equation_in_str:
                first_number, remainding = equation_in_str.split("*")
                second_number, ans = remainding.split("=")
                if int(first_number) * int(second_number) == int(ans):
                   return True
                return False
            elif "//" in equation_in_str:
                first_number, remainding = equation_in_str.split("//")
                second_number, ans = remainding.split("=")
                if int(first_number) // int(second_number) == int(ans):
                   return True
                return False
            elif "%" in equation_in_str:
                first_number, remainding = equation_in_str.split("%")
                second_number, ans = remainding.split("=")
                if int(first_number) % int(second_number) == int(ans):
                   return True
                return False

    return True
