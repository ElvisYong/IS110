# Part 2
message = list(input("What's the original message? "))
for i, char in enumerate(message):
    if char == 'a':
        message[i] = 'e'
    elif char == 'e':
        message[i] = 'i'
    elif char == 'i':
        message[i] = 'o'
    elif char == 'o':
        message[i] = 'u'
    elif char == 'u':
        message[i] = 'a'

# Part 2
reversed = message[::-1]

print("The encrypted message is '", ''.join(reversed), "'")