def transform_string(word):
    new_string = ''
    no_upper = 0
    no_lower = 0
    no_digit = 0
    no_symbol = 0    
    for i in range(len(word)):
        if word[i].isupper():
            new_string += 'L'
            no_upper += 1
        elif word[i].islower():
            new_string += 'l'
            no_lower += 1
        elif word[i].isdigit():
            new_string += 'd'
            no_digit += 1
        else:
            new_string += 's'
            no_symbol += 1
    print('Number of uppercase letters: ', no_upper)
    print('Number of lowercase letters: ', no_lower)
    print('Number of ndigits: ', no_digit)
    print('Number of symbols: ', no_symbol)
    return new_string

