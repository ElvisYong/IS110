#
# Name:
# Email ID:
#
def represent_numbers(start, end):
    # write your answer between #startcode and #endcode
    # startcode
    res = ''
    if start > 0 and end > 0:
        if start <= end:
            for i in range(start, end + 1):
                if i == end:
                    res += '-' * i
                    break
                res += '-' * i
                res += '#'
        else:
            return ''
    elif start < 0 and end > 0:
        i = start
        while i < end + 1:
            if i == end:
                res += '-' * i
                break
            res += '-' * abs(i)
            res += '#'
            i += 1

    return res
    # endcode


print('Test 1')
print('Expected:-#--#---#----#-----')
print('Actual  :' + represent_numbers(1, 5))
print()

print('Test 2')
print('Expected:---#----#-----')
print('Actual  :' + represent_numbers(3, 5))
print()

print('Test 3')
print('Expected:-')
print('Actual  :' + represent_numbers(1, 1))
print()

print('Test 4')
print('Expected:[]')
print('Actual  :[' + represent_numbers(4, 1) + ']')
print()

print('Test 5')
print('Expected:----#---#--#-##-')
print('Actual  :' + represent_numbers(-4, 1))
print()
