# Part A
# keyword = input('Enter a keyword: ')

# count = 1
# with open('news.txt', 'r') as f:
#     for line in f.readlines():
#         if keyword.lower() in line.lower():
#             print(f'{count}. {line}')
#             count +=1

# Part B
search = input('Do you want to search our news database? [Y]|[N] : ')
keyword = input('Enter a keyword: ')

while search.lower() == 'y':
    with open('news.txt', 'r') as f:
        headlines = []
        for line in f.readlines():
            print(line)
            if keyword.lower() in line.lower():
                headlines.append(line)

        if len(headlines) == 0:
            print(headlines)
            print('There is no matching headlines!')
            search = input('Do you want to search again? [Y]|[N] : ')
            if search.lower() == 'y':
                keyword = input('Enter a keyword: ')
            continue

        print(f'There are {len(headlines)} matching headliness')
        for count, item in enumerate(headlines):
            print(f'{count + 1}. {item}')

        search = input('Do you want to search again? [Y]|[N] : ')
        if search.lower() == 'y':
            keyword = input('Enter a keyword: ')
    
