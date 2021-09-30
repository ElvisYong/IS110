def is_pangram(pangram):
    pangram = pangram.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in pangram:
            return False
    return True