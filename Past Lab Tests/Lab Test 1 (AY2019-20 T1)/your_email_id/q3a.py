# Name:
# Email ID:

def calculate_entrance_fees_1(n):

    # These variables are defined for you to use.
    PACKAGE_B = 110
    PACKAGE_C = 200

    # Modify the code below.
    total_cost = 0
    max_package_c = n // 2
    remainder = n % 2

    return (PACKAGE_B * remainder) + (max_package_c * PACKAGE_C)
        