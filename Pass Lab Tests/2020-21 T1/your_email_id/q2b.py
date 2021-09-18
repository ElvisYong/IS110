# Name:
# Email ID:

def get_max_of_min(list_of_num_tuples):
    # Replace the code below with your implementation.
    
    # Note: You’re NOT allowed to use either min()or max()to solve this problem.
    if list_of_num_tuples:
        list_smoll = []
        max_smoll = None
        for i in list_of_num_tuples:
            smoll = None
            for n in i:
                if smoll == None:
                    smoll = n
                elif n < smoll:
                    smoll = n
            list_smoll.append(smoll)
        for number in list_smoll:
            if max_smoll == None:
                max_smoll = number
            elif number > max_smoll:
                max_smoll = number
        return max_smoll
    return None