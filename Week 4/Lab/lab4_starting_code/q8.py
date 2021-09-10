## Q8
# ################################################################################
# The function below is for you to implement! 
def display_fibonacci(n):
    """
    This function takes in an integer n (greater or equal to 3). It prints out the 
    first n Fibonacci numbers, starting from 1. The function doesn’t return anything.
    """
    # Modify the code below to print the first n Fibonacci numbers
    n1, n2 = 1, 1
    for i in range(1,n + 1):
        print(n1, end=' ')
        nth = n1 + n2
        n1 = n2
        n2 = nth



