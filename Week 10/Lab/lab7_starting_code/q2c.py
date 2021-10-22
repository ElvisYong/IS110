### Q2c: Universities 
# Write your code below:
def search_with_keyword(filename, keyword):
    res = []
    with open(filename, 'r') as f:
         for line in f:
            details = line.split('\t')
            if keyword.lower() in details[0].lower():
                res.append(details[1])
    return res

             





