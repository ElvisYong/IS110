# ################################################################################
# This function is for you to implement!
def calculate_tax_3(income):
    """
    This function assumes that the income is between $0 and $40,000.
    """
    tax_payable = max(((income - 30000) * 0.035 + 200), (income - 20000) * 0.02, 0) 

    return tax_payable


# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_3(25000.0))
print(calculate_tax_3(10000.0))
print(calculate_tax_3(35000.0))

# ################################################################################