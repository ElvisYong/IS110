# Part A + part B
with open('phone_book.txt', 'r') as f:
    with open('phone_book_reorganized.txt', 'w') as wf:
        num_set = {}
        for line in f.readlines():
            author, number = line.strip().split('|')
            if author not in num_set:
                num_set[author] = [number]
            else:
                num_set[author].append(number)
            if '(' in number:
                number = number.replace('(', '')
                number = number.replace(')', '')
            if '+65' in number:
                print(line)
            elif '+' not in number and len(number) == 8:
                print(line)
        for authors in num_set.items():
            wf.writelines(authors[0] + "\n")
            for i in authors[1]:
                wf.writelines(i + "\n")
            wf.writelines("\n")
        




