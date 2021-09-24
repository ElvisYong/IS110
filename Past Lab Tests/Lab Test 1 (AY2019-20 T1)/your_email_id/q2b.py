# Name:
# Email ID:

def add_even_numbers(str_list):
    # Modify the code below.
    if str_list:
        split_strings = [number for numbers in str_list for number in numbers.split('|')]
        total = 0
        for i in split_strings:
            num = int(i)
            if num % 2 == 0:
                total += num
        return total
        
    return 0