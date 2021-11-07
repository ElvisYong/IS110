def find_last_letter(my_str):
    # Modify the code below.
    latest_index = -1
    for i in range(len(my_str)):
        if not my_str[i].isdigit():
            latest_index = i

    return latest_index

    
    
if __name__ == "__main__":
    print('\nTestcase 1')
    print('-' * 10)
    my_str = '12abc345'
    print("Expected: 4")
    print('Actual:   ' + str(find_last_letter(my_str)))

    print('\nTestcase 2')
    print('-' * 10)
    my_str = '12ab345C'
    print("Expected: 7")
    print('Actual:   ' + str(find_last_letter(my_str)))

    print('\nTestcase 3')
    print('-' * 10)
    my_str = '12345'
    print("Expected: -1")
    print('Actual:   ' + str(find_last_letter(my_str)))

    print('\nTestcase 4')
    print('-' * 10)
    my_str = 'A'
    print("Expected: 0")
    print('Actual:   ' + str(find_last_letter(my_str)))

    print('\nTestcase 5')
    print('-' * 10)
    my_str = ''
    print("Expected: -1")
    print('Actual:   ' + str(find_last_letter(my_str)))