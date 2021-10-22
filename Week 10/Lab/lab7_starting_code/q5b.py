### Q5b: Matrix

# Write your code below:
def get_matrix_transpose(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            for num in line.strip().replace(' ', ''):
                row.append(float(num))
            matrix.append(row)

    new_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    return new_matrix

