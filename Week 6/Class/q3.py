def retrieve_numbers(numbers):
    new_string = ''
    for i, n in enumerate(numbers):
        if n.isdigit():
            new_string += n
        else:
            if i + 1 < len(numbers) and numbers[i+1].isdigit() and new_string != '':
                new_string += ' '
    return new_string

print(retrieve_numbers("12abc600$##0900AB 100X"))
print(retrieve_numbers("34.5689abc980"))
print(retrieve_numbers("xyz"))
print(retrieve_numbers("abc25xyz"))