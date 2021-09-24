# Name:
# Email ID:

import q3a

def calculate_entrance_fees_2(m, n):
    
    # These variables are defined for you to use.
    ADULT_TICKET = 75
    CHILD_TICKET = 50
    
    PACKAGE_A = 140
    PACKAGE_B = 110
    PACKAGE_C = 200
    
    # Modify the code below.
    if m == n:
        return q3a.calculate_entrance_fees_1(m)

    if n == 0:
        max_no_of_package_a = m // 2
        remainder = m % 2

        return (ADULT_TICKET * remainder) + (PACKAGE_A * max_no_of_package_a)
    
    a_counter = 0
    b_counter = 0
    c_counter = 0

    while (m >= 2 and n>= 2):
        m -= 2
        n -= 2
        c_counter += 1
    
    while (m >= 1 and n >= 1):
        m -= 1
        n -= 1
        b_counter += 1
    
    while (m >= 2):
        m -= 2
        a_counter += 1
    
    price = (a_counter * PACKAGE_A) + (b_counter * PACKAGE_B) + (c_counter * PACKAGE_C)
    price += (m * ADULT_TICKET) + (n * CHILD_TICKET)

    return price
 