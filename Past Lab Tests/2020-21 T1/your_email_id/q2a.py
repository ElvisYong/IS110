# Name:
# Email ID:

def get_sum_of_digits(my_str):
    # Replace the code below with your implementation.
    count = 0
    if my_str:
        for char in my_str:
            if char.isdigit():
                count += int(char)
        return count
    return 0