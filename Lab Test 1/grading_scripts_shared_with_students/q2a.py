# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021

def get_right_most_even_digit(number):
    # Replace the code below with your implementation.
    string_number = str(number)
    reversed_string = string_number[::-1]
    for number in reversed_string:
        if int(number) % 2 == 0:
            return int(number)

    return None
    