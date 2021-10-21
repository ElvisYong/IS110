### Q1b Reading Files
# Write your code below:
def print_alternate_columns(filename):
    with open(filename, 'r') as f:
        for line in f:
            items = line.strip().split('&')
            for count, item in enumerate(items):
                if count % 2 == 0:
                    if count == len(items) - 1:
                        print(item.strip())
                    else:
                        print(item.strip(), end=' & ')
        

print_alternate_columns('q1-input-3.txt')