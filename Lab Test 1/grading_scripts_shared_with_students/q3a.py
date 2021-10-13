# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021

def check_diversity(team):
    # Replace the code below with your implementation.
    race_list = []
    religion_list = []
    male_count = 0
    female_count = 0
    for members in team:
        name, gender, race, religion = members
        # gender check
        if gender == 'M':
            male_count += 1
        elif gender == 'F':
            female_count += 1
        
        # Race check
        if race not in race_list:
            race_list.append(race)
        
        # Religion check
        if religion == 'Freethinker':
            continue
        elif religion not in race_list:
            religion_list.append(religion)
        
    if not ((male_count == 3 and female_count == 2) or (male_count == 2 and female_count == 3)):
        return False
    
    if len(race_list) < 3:
        return False
    
    if len(religion_list) < 2:
        return False
        
    return True