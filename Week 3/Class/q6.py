a = input()
b = input()
print(not(not(a and not b) or (b or not a))) # test

print(not(a and b) or not (a or not b))
