# Name:
# Email ID:

def trace_contacts(patient, history):
    # Replace the code below with your implementation.
    infections = []
    for data in history:
        person_a, person_b, days = data
        if person_a == patient and days > -6 and days < 0:
            infections.append((person_b, days+2))
        elif person_b == patient and days > -6 and days < 0:
            infections.append((person_a, days+2))

    i = 0
    while i < len(infections):
        person, infection_req = infections[i]
        for data in history:
            a, b, days = data
            if person == a and days == infection_req:
                infections.append((b, days+2))
            elif person == a and days == infection_req:
                infections.append((a, days+2))
        i += 1
    

    return [i[0] for i in infections]