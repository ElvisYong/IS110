# Name:
# Email ID:

def get_longer_words(file_name):
    # Modify the code below.
    res = []
    with open(file_name, 'r') as f:
        for line in f:
            words = line.strip('\n').split('&')
            res.append(words[0] if len(words[0]) > len(words[1])
                       or len(words[0]) == len(words[1]) else words[1])
    return res
