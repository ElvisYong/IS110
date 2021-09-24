# Name:
# Email ID:

def get_number_of_long_strings(str_list, n):
    # Modify the code below.
    if str_list:
        return len([i for i in str_list if len(i) > n])
    return 0