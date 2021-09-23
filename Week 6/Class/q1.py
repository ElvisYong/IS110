# part A
def get_larger_values(x):
    total = 0
    for i in x:
        total += i
    average = total / len(x)
    larger_values = []
    for i in x:
        if i > average:
            larger_values.append(i)

    return larger_values

print(get_larger_values([2.5, 3.5, 5.5, 1.0]))

#part B
def merge_list(x, y):  
    i = 0
    merged_list = []
    if len(x) > len(y):
        while i < len(x):
            merged_list.append(x[i])
            if i < len(y):
                merged_list.append(y[i])

            i += 1
    elif len(y) > len(x):
        while i < len(y):
            merged_list.append(y[i])
            if i < len(x):
                merged_list.append(x[i])
            i += 1
    return merged_list

print(merge_list([1, 3, 10, 15, 4, 7, 12], [9,5,2]))

#part c
def check_numbers(int_list_1, int_list_2):
    for i in int_list_1:
        if all(i % x != 0 for x in int_list_2):
            return False
    return True

print(check_numbers([3,8,10,15,16], [9,3,2,5]))
print(check_numbers([3,8,10,6,2,5], [9,3,7]))