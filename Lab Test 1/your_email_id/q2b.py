# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021

def get_all_third_digits(str_list):
    # Replace the code below with your implementation.
    count = 1
    res = []
    for words in str_list:
        for char in words:
            if char.isnumeric():
                if count == 3:
                    res.append(int(char))
                    break
                else:
                    count += 1
        count = 1

    return res