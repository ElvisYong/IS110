## Q1a Substitution Cipher
# write your code below
def encrypt(my_dict, msg):
    new_msg = ''
    for char in msg:
        if char.isalpha():
            new_msg += my_dict[char]
        else:
            new_msg += char
    return new_msg
