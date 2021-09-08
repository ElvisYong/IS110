def compute_sum_recursion(m, n):
    """
    computes the sum of all integers between m and n
    """
    if m > n:
        return 0
    else:
        return m + compute_sum_recursion(m + 1, n)

print(compute_sum_recursion(1, 10))

def compute_sum_iteration(m, n):
    """
    computes the sum of all integers between m and n
    """
    sum = 0
    for i in range(m, n + 1):
        sum += i
    return sum

my_sum = compute_sum_iteration(4, 10)
print("The sum is " + str(my_sum))