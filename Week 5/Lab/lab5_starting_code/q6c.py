### Q6 More on Lists
## c)
# Write your code below:
##############################################################
def get_non_common_strings(str_list1, str_list2):
    res = []
    for i in str_list1:
        if i not in str_list2:
            res.append(i)
    
    for i in str_list2:
        if i not in str_list1:
            res.append(i)
    return res








##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()