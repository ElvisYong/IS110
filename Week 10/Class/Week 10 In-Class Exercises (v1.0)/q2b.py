def same_author(file_name):
    with open(file_name, 'r') as f:
        first_author = ''
        for line in f.readlines():
            author = line.strip().split('$')[0].split()[-1]
            if first_author == '':
                first_author = author
                continue
            if author != first_author:
                return False
    return True
        
# Test cases used to test your function
print('\nTestcase 1')
print('-' * 10)
print("Expected: False")
filename = 'books-1.txt'
result = same_author(filename)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: True")
filename = 'books-2.txt'
result = same_author(filename)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print("Expected: False")
filename = 'books-3.txt'
result = same_author(filename)
print('Actual:   ' + str(result))

