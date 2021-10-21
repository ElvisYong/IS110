## Q1 Reading Files
# Write your code below:
##############################
def print_alternate_lines(filename):
    with open(filename, 'r') as f:
        i = 0
        lines = f.readlines()
        while i < len(lines) - 1:
            print(lines[i].rstrip())
            i += 2
