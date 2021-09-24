# =====
# q2.py
# =====
# Name: Yong Yu En, Elvis 
# Email ID: elvis.yong.2021

def display_strings(str_list, ch):
    # Modify the code below
    if str_list:
        no_of_items = len(str_list) - 1
        max_length_of_word = max(len(i) for i in str_list)

        for count, i in enumerate(str_list):
            if count == len(str_list) - 1:
                spaces = ''
            else:
                spaces = ' ' * no_of_items 
            print(spaces + i + ch * (max_length_of_word - len(i)))
            no_of_items -= 1
