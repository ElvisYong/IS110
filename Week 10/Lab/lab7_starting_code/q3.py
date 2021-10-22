with open('temperatures.txt', 'r') as f:
    for line in f:
        name = line.rstrip().split('\t')[0]
        details = line.rstrip().split('\t')[1:]
        print(f'{name}, {min(details)}, {max(details)}')