# Q1 Initials
# Write your code below:
##############################
no_of_initials = int(input("Enter the number of initials: "))
initials = []
for i in range(no_of_initials):
    name = input(f"Participant {i + 1}: ")
    name_split = name.split(' ')
    joined_initial = ''
    for n in name_split:
        joined_initial += n[0]
    initials.append(joined_initial)

for i in initials:
    print(i)