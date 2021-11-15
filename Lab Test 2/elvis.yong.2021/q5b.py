# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021

def get_seating(person_list, n, m):
    pass
    # Write your code here.
    

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, person_list, n, m, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_seating("{person_list}", {n}, {m})')
        print()
        print('Note that there can be many other correct outputs not listed here.')
        print(f'Expected: {expected_output}.')
        result = get_seating(person_list, n, m)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        
    person_list = [('john', 'M'), ('val', 'F'), ('ann', 'F'), ('alex', 'F'), ('don', 'M')]
    expected_list = [('john', 'M'), ('val', 'F'), ('ann', 'F'), ('don', 'M'), ('alex', 'F')]
    run_test_case(1, person_list, 3, 2, expected_list, "<class 'list'>")

    person_list = [('john', 'M'), ('val', 'F'), ('ann', 'F'), ('alex', 'F'), ('don', 'M')]
    expected_list = []
    run_test_case(2, person_list, 3, 3, expected_list, "<class 'list'>")

    person_list = [('john', 'M'), ('val', 'F'), ('ann', 'F'), ('don', 'M'), ('alex', 'F')]
    expected_list = [('john', 'M'), ('val', 'F'), ('ann', 'F'), ('don', 'M'), ('alex', 'F')]
    run_test_case(3, person_list, 3, 2, expected_list, "<class 'list'>")

    person_list = [('a', 'M'), ('b', 'M'), ('c', 'M'), ('d', 'M'), ('e', 'F'), ('f', 'F'), ('g', 'F'), ('h', 'F')]
    expected_list = [('a', 'M'), ('b', 'M'), ('c', 'M'), ('e', 'F'), ('d', 'M'), ('f', 'F'), ('g', 'F'), ('h', 'F')]
    run_test_case(4, person_list, 4, 2, expected_list, "<class 'list'>")