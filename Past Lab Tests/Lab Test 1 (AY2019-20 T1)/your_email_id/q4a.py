# Name:
# Email ID:

def check_seating_arrangement(arrangement, must_list, cannot_list):
    # Modify the code below.
    all_permutations = []
    i = 0
    while i < len(arrangement) - 1:
        if i == 0:
            all_permutations.append((arrangement[i], arrangement[+1]))
            all_permutations.append((arrangement[i], arrangement[-1]))
        elif i == len(arrangement) - 1:
            all_permutations.append((arrangement[i], arrangement[i - 1]))
            break
        else:
            all_permutations.append((arrangement[i], arrangement[i + 1]))
            all_permutations.append((arrangement[i], arrangement[i - 1]))
        i += 1

    for seatings in all_permutations:
        if seatings in cannot_list:
            return False
        if seatings in must_list:
            must_list.remove(seatings)
        
    if must_list == []:
        return True

    return False
 