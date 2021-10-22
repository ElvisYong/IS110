### Q5a: Matrix

# Write your code below:
def get_matrix(filename):
    res = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            for num in line.strip().replace(' ', ''):
                row.append(float(num))
            res.append(row)
    return res



