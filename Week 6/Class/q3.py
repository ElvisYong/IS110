def retrieve_numbers(numbers):
    new_string = ''
    i = 0
    while i < len(numbers) - 1:
        if numbers[i].isnumeric():
            new_string += numbers[i]
        else:
            if i + 1 < len(numbers) and numbers[i+1].isdigit() and new_string != '':
                new_string += ' '
        i += 1
    return new_string

print(retrieve_numbers("12abc600$##0900AB 100X"))
print(retrieve_numbers("34.5689abc980"))
print(retrieve_numbers("xyz"))
print(retrieve_numbers("abc25xyz"))