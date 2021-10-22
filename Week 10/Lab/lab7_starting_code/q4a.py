with open('transactions.txt', 'r') as rf:
    with open('transactions-output-1.txt', 'w') as wf:
        for line in rf:
            price = float(line.rstrip().split('$')[1])
            if price > 30:
                wf.write(line)

