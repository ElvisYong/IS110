### Q2a: Universities 
# Write your code below:
def get_universities_founded_before(filename, year):
    with open(filename, 'r') as f:
        match_uni = []
        for line in f:
            details = line.split('\t')
            if int(details[2]) < year:
                match_uni.append(details[0])
    return match_uni



