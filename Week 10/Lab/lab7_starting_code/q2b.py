### Q2b: Universities 
# Write your code below:
def get_average_num_students(filename):
    with open(filename, 'r') as f:
        total = 0
        count = 0
        for lines in f:
            details = lines.split('\t')
            total += int(details[3])
            count+=1
        
        return total/count