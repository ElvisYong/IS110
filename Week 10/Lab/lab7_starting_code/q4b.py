from datetime import datetime

dates = []
with open('transactions.txt', 'r') as rf:
    for line in rf:
        dates.append(line)

dates.sort(key = lambda date: datetime.strptime(date.strip().split('\t')[0], '%d-%m-%Y'))

month = ''
cur_month = []
total_spendings = 0.0
with open('transactions-output-2.txt', 'w') as wr:
    for items in dates:
        details = items.strip().split('\t')
        display_month = details[0].split('-')[1] + '-' + details[0].split('-')[2]

        if month == '':
            total_spendings += float(items.strip().split('$')[1])
            month = display_month
            cur_month.append(details)

        elif month == display_month:
            total_spendings += float(items.strip().split('$')[1])
            cur_month.append(details)
        
        else:
            wr.write('\n')
            wr.write(f'{month}: total transaction amount is ${total_spendings}' + '\n')
            for i in cur_month:
                wr.write(f'{i[1]} ${i[2]}')
                wr.write('\n')
            month = display_month
            total_spendings = float(items.strip().split('$')[1])
            cur_month = []
            cur_month.append(details)





        
            

            