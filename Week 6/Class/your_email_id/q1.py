# =====
# q1.py
# =====
# Name: Yong Yu En, Elvis  
# Email ID: elvis.yong.2021

def add_first_odd_digits(str_list):
    # modify the code below
    total = 0
    for words in str_list:
        for i in words:
            if i.isdigit() and int(i) % 2 != 0:
                total += int(i)
                break
    return total