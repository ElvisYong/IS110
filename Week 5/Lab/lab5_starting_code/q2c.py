### Q2 List of Numbers
## c)
# Write your code below:
##############################################################
def get_sum_multiples(int_list, n):
    """
    Returns the sum of all the multiples of the numbers in int_list
    """
    sum = 0
    for i in int_list:
        if i % n == 0:
            sum += i
    return sum





##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: 24')
print('Actual:   ' + str(get_sum_multiples([2, 4, 5, 9, 13, 15], 3)))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 20')
print('Actual:   ' + str(get_sum_multiples([2, 4, 5, 9, 13, 15], 5)))
