def process_numbers(input_filename, output_filename):
    # Modify the code below.
    grp_count = 0
    with open(input_filename, 'r') as input_file:
        with open(output_filename, 'w') as output_file:
            for line in input_file:
                grps = line.split('#')
                average = 0
                output_file.write(f'{len(grps)}:')
                for grp in grps:
                    # find average number in each group
                    words = grp.split(' ')
                    sum_words = sum([float(word) for word in words])
                    average =  sum_words / len(words)
                    output_file.write(f'{average}')
                output_file.write(f'{len(grps)}:')
                

    pass

if __name__ == "__main__":
    # print("Test Case for Q3")
    # print()

    process_numbers("numbers.txt", "output.txt")
    print("Please check whether the file 'output.txt' generated is the same as the file 'expected-output.txt' that we've provided.")