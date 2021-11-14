# Name:
# Email ID:

def compute_product(num_list):
    # Modify the code below.
    res = 1
    if num_list:
        for num in num_list:
            if num % 2 != 0:
                res *= num

    return res
    