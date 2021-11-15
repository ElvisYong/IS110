# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021
def read_schedule(filename):
    pass
    # Write your code here.
    res = {}
    names = {}
    with open(filename, 'r') as f:
        for line in f:
            split_line = line.strip().split('|')
            day, start_time, end_time, name = split_line[0], split_line[1], split_line[2], split_line[3]

            # Convert start_time and end_time to 24 hour format
            new_start_time = ''
            new_end_time = ''
            if 'PM' in start_time:
                for char in start_time:
                    if char.isnumeric and not char.isalpha():
                        new_start_time += char
                new_start_time = int(new_start_time) + 12
            else:
                for char in start_time:
                    if char.isnumeric and not char.isalpha():
                        new_start_time += char
                new_start_time = int(new_start_time)
            if 'PM' in end_time:
                for char in end_time:
                    if char.isnumeric and not char.isalpha():
                        new_end_time += char
                new_end_time = int(new_start_time) + 12
            else:
                for char in end_time:
                    if char.isnumeric and not char.isalpha():
                        new_end_time += char
                new_end_time = int(new_end_time)
            
            # Populate names with time into names
            if ' ' in name:
                name = name.split(' ')
                for n in name:
                    if n in names:
                        names[n].append((day, new_start_time, new_end_time))
                    else:
                        names[n] = [(day , new_start_time, new_end_time)]
            else:
                if name in names:
                    names[name].append((day, new_start_time, new_end_time))
                else:
                    names[name] = [(day , new_start_time, new_end_time)]
    
    for name in names:
        shifts = names[name]
        for shift in shifts:
            day, start_time, end_time = shift
            if day in res:
                res[day].append((start_time, end_time, name))
            else:
                res[day] = [(start_time, end_time, name)]
    return res


# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, filename, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: read_schedule("{filename}")')
        print()
        print(f'Expected: {expected_output}')
        result = read_schedule(filename)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
    
    expected_dict =  {'Mon': [(9, 10, 'ahbeng'), (9, 16, 'donta'), (10, 17, 'starkov'), (9, 16, 'leongben')], 'Tue': [(12, 17, 'jingjiang'), (12, 17, 'michellekan'), (9, 17, 'leongben'), (9, 17, 'darkling'), (14, 16, 'markloh'), (14, 16, 'angelwong')], 'Wed': [(9, 12, 'markloh'), (9, 12, 'vandana'), (13, 14, 'wendytan'), (9, 12, 'ylee'), (9, 12, 'wangyong'), (13, 14, 'joelle')], 'Fri': [(14, 17, 'tonytan'), (14, 17, 'jessicali')]}
    run_test_case(1, 'schedule1.txt' , expected_dict, "<class 'dict'>")

    expected_dict = {'Mon': [(9, 11, 'ahbeng'), (9, 11, 'donta')], 'Thu': [(12, 17, 'qianru')], 'Sat': [(9, 12, 'markloh'), (9, 12, 'haewoon')], 'Sun': [(13, 17, 'wangyong')]}
    run_test_case(2, 'schedule2.txt' , expected_dict, "<class 'dict'>")
