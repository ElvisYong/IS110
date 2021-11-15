# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021
def extract_names_2(name_list):
    
    pass
    # Write your code here.
    res = []
    for name in name_list:
        new_name = ''
        for char in name:
            if char == ' ' or char.isalpha():
                new_name += char
        if not new_name.isspace():
            res.append(new_name)

    return res


# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, name_list, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: extract_names_2({name_list})')
        print()
        print(f'Expected: {expected_output}')
        result = extract_names_2(name_list)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
    
    run_test_case(1, ['Alex T5an', '^Harry Potter$', 'Squid$$ Game', 'abc','5 -6- 7-8'], ['Alex Tan', 'Harry Potter', 'Squid Game', 'abc'], "<class 'list'>")
    run_test_case(2, ['Alina Star**kov', 'Jessie Mei   Li'], ['Alina Starkov', 'Jessie Mei   Li'], "<class 'list'>")
    run_test_case(3, ['@@ 12'], [], "<class 'list'>")
    run_test_case(4, [], [], "<class 'list'>")
