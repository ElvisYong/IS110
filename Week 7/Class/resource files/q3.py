# part a
def print_triangle(ch, num_rows):
    spaces = num_rows - 1
    count = 1
    for i in range(0, num_rows):
        if i == 0:
            print((' ' * spaces) + ch)
        else:
            print((' ' * spaces) + ch * (i + count))
        spaces -= 1
        count += 1

def print_frame(ch, num_rows, num_cols):
    for i in range(0, num_rows):
        if i == 0 or i == num_rows - 1:
            print(ch * num_cols)
        else:
            print(ch + (' ' * (num_cols - 2)) + ch)

