def check_numbers(int_list_1, int_list_2):
    for i in range(len(int_list_1)):
        num1 = int_list_1[i]
        for i in range(len(int_list_2)):
            num2 = int_list_2[i]
            if num1 % num2 == 0:
                valid = True
                break 
            elif num1 % num2 != 0:
                valid = False
    print(valid)
            
print(check_numbers([3, 8, 10, 15, 16], [9, 3, 2, 5]) )
print(check_numbers([3, 8, 10, 6, 2, 5], [9, 3, 7]))