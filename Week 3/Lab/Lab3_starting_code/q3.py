## Q3 PART 1
# This function is for you to implement!
def calculate_salary(monthly_sales):
    
    # This variable is defined for you to use.
    BASE_SALARY = 2000.0
    
    # ################################################################################
    # Modify the code below to return the right amount of salary.
    if(monthly_sales < 10000):
        return (monthly_sales * 0.05) + BASE_SALARY
    elif(monthly_sales >= 10000 and monthly_sales < 15000):
        return (monthly_sales * 0.10) + BASE_SALARY
    elif(monthly_sales >= 15000 and monthly_sales < 18000):
        return (monthly_sales * 0.15) + BASE_SALARY
    elif(monthly_sales >= 18000):
        return (monthly_sales * 0.18) + BASE_SALARY
    
    return BASE_SALARY
    # ################################################################################

## Q3 PART 2
# Write your code below
monthly_sales = int(input("Enter the monthly sales: "))
print("The monthly pay for the sales person is $",calculate_salary(monthly_sales))


