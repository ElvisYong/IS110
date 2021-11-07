def find_second_letter(my_str):
    # Write your code below
    count = 0
    for i in range(len(my_str)):
        if not my_str[i].isdigit():
            if count == 1:
                return i
            count += 1
    return -1
        

if __name__ == "__main__":
    # Test Cases of Q1b
    print('\nTestcase 1')
    print('-' * 10)
    my_str = '12abc345'
    print("Expected: 3")
    print('Actual:   ' + str(find_second_letter(my_str)))

    print('\nTestcase 2')
    print('-' * 10)
    my_str = 'ABcd'
    print("Expected: 1")
    print('Actual:   ' + str(find_second_letter(my_str)))

    print('\nTestcase 3')
    print('-' * 10)
    my_str = '12345'
    print("Expected: -1")
    print('Actual:   ' + str(find_second_letter(my_str)))

    print('\nTestcase 4')
    print('-' * 10)
    my_str = 'A'
    print("Expected: -1")
    print('Actual:   ' + str(find_second_letter(my_str)))

    print('\nTestcase 5')
    print('-' * 10)
    my_str = ''
    print("Expected: -1")
    print('Actual:   ' + str(find_second_letter(my_str)))