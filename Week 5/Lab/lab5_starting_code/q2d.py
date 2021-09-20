### Q2 List of Numbers
## d)
# Write your code below:
##############################################################
def is_prime(num):
    """
    This function takes a number and returns True if the number is prime,
    False otherwise.
    :param num: A number
    :return: True if the number is prime, False otherwise
    """
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_prime_numbers(num_list, sep = " "):
    """
    This function takes a list of numbers and returns a list of prime numbers.
    :param num_list: A list of numbers
    :param sep: A separator between numbers
    :return: A list of prime numbers
    """
    prime_list = ''
    for i, num in enumerate(num_list):
        if is_prime(num):
            if prime_list == '':
                primte_list = str(num)
            else:
                prime_list += sep + str(num)
    return prime_list






##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: 2-7-11-19')
print('Actual:   ' + str(get_prime_numbers([2, 4, 7, 9, 11, 16, 19, 21], '-')))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 3')
print('Actual:   ' + str(get_prime_numbers([3, 4, 8, 9, 12, 16], '*')))
