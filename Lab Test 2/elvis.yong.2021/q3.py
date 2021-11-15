# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021
import datetime
def get_days_between(start_tup, end_tup):
    '''
    This function returns the number of days between two dates.
    Do not modify the code in this function!!!
    You're required to use this function in your code for Q3.
    
    Parameters:
        start_tup: the start date which is a tuple in the form (year, month, day).
             The year, month and day are integers.
        end_tup:   the end date. The format is the same as start_tup.

    Returns the number of days in between the 2 days (end_tuple – start_tuple).
    For example, if start_tup is (2020, 12, 1) and end_tup is (2020, 12, 3), this
    function returns the value 2.

    More examples:
    get_days_between((2021,10,15), (2021, 10, 30)) returns 15
    get_days_between((2021,8,15), (2021, 10, 11)) returns 57
    get_days_between((2021,8,15), (2021, 9, 12)) returns 28
    get_days_between((2021,10,15), (2021, 10, 29)) returns 14
    '''

    start_date = datetime.date(*start_tup)
    end_date = datetime.date(*end_tup)
    return (end_date - start_date).days


    
def get_vaccination_status(filename, today):
    
    pass
    # Write your code here.
    # store everything in a tuple
    people = {}
    today = today.split('/')
    today = (int(today[2]), int(today[1]), int(today[0]))
    with open(filename, 'r') as f:
        for line in f:
            data = line.strip().split('|')
            name, age, first_date, second_date = data[0], int(data[1]), data[2], data[3]

            if first_date == 'NA' or second_date == 'NA' or age < 12:
                people[name] = (age, False)
                continue
            
            # Extract date into tuples
            first_date = first_date.split('/')
            second_date = second_date.split('/')

            first_date = (int(first_date[2]), int(first_date[1]), int(first_date[0]))
            second_date = (int(second_date[2]), int(second_date[1]), int(second_date[0]))

            days_between_doses = get_days_between(first_date, second_date)
            days_after_second = get_days_between(second_date, today)

            if (days_between_doses < 28 and days_between_doses > 56):
                people[name] = (age, False)
                continue
            
            if days_after_second < 14:
                people[name] = (age, False)
                continue

            people[name] = (age, True)
            
    return people

    

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, filename, today, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_vaccination_status("{filename}", "{today}")')
        print()
        print(f'Expected: {expected_output}')
        result = get_vaccination_status(filename, today)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
        
    
    expected_dict = {'S1': (22, True), 'F1': (2, False), 'G2': (35, False), 'S2': (12, True), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(1, 'record1.txt', '25/10/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'S1': (22, True), 'F1': (2, False), 'G2': (35, True), 'S2': (12, True), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(2, 'record1.txt', '15/11/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'S1': (22, False), 'F1': (2, False), 'G2': (35, False), 'S2': (12, False), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(3, 'record1.txt', '15/1/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'F1': (2, False), 'S2': (11, False), 'S3': (8, False)}
    run_test_case(4, 'record2.txt', '15/10/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'G2': (35, False), 'S3': (22, False), 'S4': (62, False)}
    run_test_case(5, 'record3.txt', '1/11/2021' , expected_dict, "<class 'dict'>")
    
