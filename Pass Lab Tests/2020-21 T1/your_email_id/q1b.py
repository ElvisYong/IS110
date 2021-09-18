# Name:
# Email ID:

def is_compatible(patient_group, donor_group):
    # Replace the code below with your implementation.
    if patient_group == "A":
        if donor_group == "B" or donor_group == "AB":
            return True
        return False
    if patient_group == "B":
        if donor_group == "B" or donor_group == "AB":
            return True
        return False
    if patient_group == "AB":
        if donor_group == "AB":
            return True
        return False
    if patient_group == "O":
        if donor_group == "O" or donor_group == "A" or donor_group == "B" or donor_group == "AB":
            return True
        return False
    return None
