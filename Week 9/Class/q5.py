def get_strings_with_digits(str_list, t):
    count = 0
    res = []
    for i in str_list:
        for j in i:
            if j.isdigit():
                count += 1
        res.append(i)
        if count > t:
            return res
        
print(get_strings_with_digits(['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn'], 5))