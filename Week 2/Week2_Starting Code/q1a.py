# ################################################################################
# The following code is given to you.
def compute_average(a, b, c):
    """
    This function returns the average of the three numbers a, b and c.
    """
    return (a + b + c)/3

# ################################################################################    
# Write your code below:

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
print("Average: ", compute_average(a, b, c))