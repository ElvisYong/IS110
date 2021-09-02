def get_middle(a, b ,c):
    highest_number = max(a, b, c)
    lowest_number = min(a, b, c)
    return a + b + c - highest_number - lowest_number

print(get_middle(1, 5, 2))