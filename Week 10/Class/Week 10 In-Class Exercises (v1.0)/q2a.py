def get_books_cheaper_than(input_file, price_limit, output_file):
    with open(input_file, 'r') as i_f:
        with open(output_file, 'w') as o_f:
            for line in i_f.readlines():
                price = float(line.split('$')[1])
                if price < price_limit:
                    o_f.write(line)

# Test cases used to test your function
print('\nTestcase 1')
print('-' * 10)
print("Expected: " + '\nTurtles All the Way Down\tJohn Green\t$11.99\n' + 
      'Animal Farm and 1984\tGeorge Orwell\t$7.50\n' + 
      'Inception: A Dark Paranormal Romance (The Marked Book 1)\tBianca Scardoni\t$13.09\n')
input_file = 'books-1.txt'
output_file = 'books-1-output.txt'
price_limit = 15.0
get_books_cheaper_than(input_file, price_limit, output_file)
result = 'Open the file books-1-output.txt and verify it contains the expected books listed above.'
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: Empty file")
input_file = 'books-2.txt'
output_file = 'books-2-output.txt'
price_limit = 7.0
get_books_cheaper_than(input_file, price_limit, output_file)
result = 'Open the file books-2-output.txt and verify it is empty.'
print('Actual:   ' + str(result))
