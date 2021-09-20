### Q6 More on Lists
## b)
# Write your code below:
##############################################################
def get_larger_numbers(num_list1, num_list2):
    """
    This function takes two lists of numbers as arguments and returns a
    list of the larger numbers between the two lists.
    """
    larger_numbers = []
    for i in num_list1:
        if all(i > j for j in num_list2):
            larger_numbers.append(i)
    return larger_numbers




##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()
