def create_num_file(output_file, n):
    with open(output_file, 'w') as f:
        for i in range(n+1):
            if i % 2 == 0:
                f.write(str(i) + '\n')

create_num_file('output.txt', 10)