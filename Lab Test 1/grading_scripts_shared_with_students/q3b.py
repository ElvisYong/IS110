# Name: Yong Yu En, Elvis
# Email ID: elvis.yong.2021

import q3a


def swap_members(team1, team2):
    # Replace the code below with your implementation.
    new_team1 = []
    new_team2 = []
    for i in team1:
        new_team1.append(i)
    for i in team2:
        new_team2.append(i)
    
    for i, member_1 in enumerate(team1):
        for j, member_2 in enumerate(team2):
            # original_member1 = team1[i]
            # original_member2 = team2[j]
            # team1[i] = original_member2
            # team2[j] = original_member1
            new_team1[i] = member_2
            new_team2[j] = member_1

            if q3a.check_diversity(new_team2) == True and q3a.check_diversity(team1) == True:
                return (member_1[0], member_2[0])

    return None